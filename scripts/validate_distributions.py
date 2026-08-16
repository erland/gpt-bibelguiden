#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, re, tempfile, zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SEMVER = re.compile(r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:-[0-9A-Za-z.-]+)?(?:\+[0-9A-Za-z.-]+)?$")
KNOWLEDGE = sorted((ROOT / "knowledge").glob("*.md"))
TEMPLATES = sorted((ROOT / "templates").glob("*.md"))
EXAMPLES = sorted((ROOT / "examples").glob("*.md"))


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def assert_same(zf: zipfile.ZipFile, member: str, src: Path) -> None:
    actual = zf.read(member)
    expected = src.read_bytes()
    if actual != expected:
        raise RuntimeError(f"Innehåll skiljer sig: {member} != {src.relative_to(ROOT)}")


def validate(version: str, dist: Path) -> None:
    if not SEMVER.fullmatch(version):
        raise RuntimeError(f"Ogiltig version: {version}")
    custom_path = dist / f"bibelguiden-custom-gpt-v{version}.zip"
    chat_path = dist / f"bibelguiden-chat-v{version}.zip"
    for p in (custom_path, chat_path):
        if not p.is_file():
            raise RuntimeError(f"Saknad distribution: {p}")
        with zipfile.ZipFile(p) as zf:
            bad = zf.testzip()
            if bad:
                raise RuntimeError(f"Korrupt ZIP-medlem i {p.name}: {bad}")

    with zipfile.ZipFile(custom_path) as zf:
        assert_same(zf, "gpt/instructions.md", ROOT / "gpt/instructions.md")
        assert_same(zf, "gpt/conversation-starters.md", ROOT / "gpt/conversation-starters.md")
        for src in KNOWLEDGE + TEMPLATES + EXAMPLES:
            assert_same(zf, src.relative_to(ROOT).as_posix(), src)
        if zf.read("VERSION").decode().strip() != version:
            raise RuntimeError("Fel VERSION i Custom GPT-paketet")

    with zipfile.ZipFile(chat_path) as zf:
        assert_same(zf, "assistant/instructions.md", ROOT / "gpt/instructions.md")
        assert_same(zf, "assistant/conversation-starters.md", ROOT / "gpt/conversation-starters.md")
        for src in KNOWLEDGE + TEMPLATES + EXAMPLES:
            assert_same(zf, src.relative_to(ROOT).as_posix(), src)
        if zf.read("VERSION").decode().strip() != version:
            raise RuntimeError("Fel VERSION i portable-paketet")
        manifest = json.loads(zf.read("MANIFEST.json"))
        if manifest.get("version") != version:
            raise RuntimeError("Fel version i MANIFEST.json")
        for member, expected_hash in manifest.get("sha256", {}).items():
            if digest(zf.read(member)) != expected_hash:
                raise RuntimeError(f"SHA-256 stämmer inte för {member}")

    print(f"Validering OK för Bibelguiden v{version}")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dist", default=str(ROOT / "dist"))
    ap.add_argument("--version")
    args = ap.parse_args()
    version = args.version or (ROOT / "VERSION").read_text(encoding="utf-8").strip()
    validate(version, Path(args.dist))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
