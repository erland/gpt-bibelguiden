#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, re, shutil, tempfile, zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SEMVER = re.compile(r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:-[0-9A-Za-z.-]+)?(?:\+[0-9A-Za-z.-]+)?$")
FIXED_DT = (2020, 1, 1, 0, 0, 0)

KNOWLEDGE = sorted((ROOT / "knowledge").glob("*.md"))
TEMPLATES = sorted((ROOT / "templates").glob("*.md"))
EXAMPLES = sorted((ROOT / "examples").glob("*.md"))


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def copy_file(src: Path, dst: Path) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(src, dst)


def write_zip(src_dir: Path, out: Path) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(out, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        for p in sorted(x for x in src_dir.rglob("*") if x.is_file()):
            rel = p.relative_to(src_dir).as_posix()
            info = zipfile.ZipInfo(rel, FIXED_DT)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            zf.writestr(info, p.read_bytes(), compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)


def build_custom(stage: Path, version: str) -> None:
    for rel in ["README.md", "gpt/instructions.md", "gpt/conversation-starters.md", "gpt/gpt-builder-config.md", "docs/creator-notes.md"]:
        copy_file(ROOT / rel, stage / rel)
    for src in KNOWLEDGE + TEMPLATES + EXAMPLES:
        copy_file(src, stage / src.relative_to(ROOT))
    (stage / "VERSION").write_text(version + "\n", encoding="utf-8")


def build_chat(stage: Path, version: str) -> None:
    copy_file(ROOT / "portable/START-HERE.md", stage / "START-HERE.md")
    copy_file(ROOT / "gpt/instructions.md", stage / "assistant/instructions.md")
    copy_file(ROOT / "gpt/conversation-starters.md", stage / "assistant/conversation-starters.md")
    for src in KNOWLEDGE + TEMPLATES + EXAMPLES:
        copy_file(src, stage / src.relative_to(ROOT))
    (stage / "VERSION").write_text(version + "\n", encoding="utf-8")
    files = {}
    for p in sorted(x for x in stage.rglob("*") if x.is_file() and x.name != "MANIFEST.json"):
        files[p.relative_to(stage).as_posix()] = sha256(p)
    manifest = {
        "package": "bibelguiden",
        "format": "portable-chat-assistant",
        "version": version,
        "entrypoint": "START-HERE.md",
        "instructions": "assistant/instructions.md",
        "conversation_starters": "assistant/conversation-starters.md",
        "knowledge": [f"knowledge/{p.name}" for p in KNOWLEDGE],
        "templates": [f"templates/{p.name}" for p in TEMPLATES],
        "examples": [f"examples/{p.name}" for p in EXAMPLES],
        "sha256": files,
    }
    (stage / "MANIFEST.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--output-dir", default=str(ROOT / "dist"))
    ap.add_argument("--version")
    args = ap.parse_args()
    version = args.version or (ROOT / "VERSION").read_text(encoding="utf-8").strip()
    if not SEMVER.fullmatch(version):
        raise SystemExit(f"Ogiltig version: {version!r}. Förväntar SemVer utan inledande v.")
    if len(KNOWLEDGE) != 9:
        raise SystemExit(f"Förväntade 9 Knowledge-filer, hittade {len(KNOWLEDGE)}")
    if len(TEMPLATES) != 5:
        raise SystemExit(f"Förväntade 5 template-filer, hittade {len(TEMPLATES)}")
    out = Path(args.output_dir)
    out.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as td:
        base = Path(td)
        custom = base / "custom"
        chat = base / "chat"
        build_custom(custom, version)
        build_chat(chat, version)
        write_zip(custom, out / f"bibelguiden-custom-gpt-v{version}.zip")
        write_zip(chat, out / f"bibelguiden-chat-v{version}.zip")
    print(f"Byggde Bibelguiden-distributioner v{version} i {out}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
