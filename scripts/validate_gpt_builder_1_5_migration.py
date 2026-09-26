#!/usr/bin/env python3
from pathlib import Path
import yaml

ROOT=Path(__file__).resolve().parents[1]

def main() -> int:
    errors=[]
    status=yaml.safe_load((ROOT/"migration-status-1.5.yaml").read_text(encoding="utf-8"))
    project=yaml.safe_load((ROOT/"gpt-project.yaml").read_text(encoding="utf-8"))
    registry=yaml.safe_load((ROOT/"runtime-distribution-registry.yaml").read_text(encoding="utf-8"))
    canonical=(ROOT/project["instructions"]["canonical"]).read_bytes()
    legacy=(ROOT/project["instructions"]["legacy_source"]).read_bytes()
    text=canonical.decode("utf-8")
    version=(ROOT/"VERSION").read_text(encoding="utf-8").strip()
    readme=(ROOT/"README.md").read_text(encoding="utf-8")

    progress=status.get("progress",{})
    if progress.get("last_completed_step")!=7:
        errors.append("migration last_completed_step must be 7")
    if progress.get("completed_steps")!=list(range(1,8)):
        errors.append("migration completed_steps must be exactly 1..7")
    if status.get("final_readiness",{}).get("migration_steps_complete")!=7:
        errors.append("final readiness must declare 7/7")
    if canonical!=legacy:
        errors.append("canonical instruction diverges from legacy instruction")
    if version!="1.0.0":
        errors.append(f"VERSION changed: {version!r}")

    if len(list((ROOT/"knowledge").glob("*.md")))!=9:
        errors.append("expected exactly 9 Knowledge files")
    if len(list((ROOT/"templates").glob("*.md")))!=5:
        errors.append("expected exactly 5 template files")
    if len(list((ROOT/"examples").glob("*.md")))!=3:
        errors.append("expected exactly 3 example files")

    if registry.get("active_targets")!=["chat","custom-gpt"]:
        errors.append(f"unexpected active targets: {registry.get('active_targets')}")
    for name in ("claude","opencode","openai_plugin"):
        if name not in registry.get("inactive_targets",{}):
            errors.append(f"missing inactive runtime decision: {name}")

    critical=[
        "ställ högst 3 följdfrågor åt gången",
        "Återge inte långa bibelavsnitt från moderna upphovsrättsskyddade översättningar.",
        "Skilj alltid mellan bibeltext, historisk bakgrund, språkliga observationer, teologisk tolkning och praktisk tillämpning.",
        "Standard: ekumeniskt och balanserat.",
        "När tolkningar skiljer sig:",
        "Skapa tydlig Markdown med konsekventa rubriker, listor och länkar.",
    ]
    for marker in critical:
        if marker not in text:
            errors.append(f"canonical behavior marker missing: {marker}")

    if "7/7 komplett" not in readme:
        errors.append("README does not state completed GPT Builder 1.5 migration")

    if errors:
        print("GPT BUILDER 1.5 MIGRATION: FAIL")
        for e in errors: print("-",e)
        return 1

    print("GPT BUILDER 1.5 MIGRATION: PASS")
    print("7/7 complete; VERSION 1.0.0; 9 Knowledge; 5 templates; 3 examples; source/theology/dialog/output behavior preserved")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
