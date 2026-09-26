#!/usr/bin/env python3
from pathlib import Path
import yaml

ROOT=Path(__file__).resolve().parents[1]

def main() -> int:
    errors=[]
    contract=yaml.safe_load((ROOT/"gpt-builder-1.5-contract.yaml").read_text(encoding="utf-8"))
    project=yaml.safe_load((ROOT/"gpt-project.yaml").read_text(encoding="utf-8"))
    canonical=(ROOT/project["instructions"]["canonical"]).read_bytes()
    legacy=(ROOT/project["instructions"]["legacy_source"]).read_bytes()
    text=canonical.decode("utf-8")
    version=(ROOT/"VERSION").read_text(encoding="utf-8").strip()

    if contract["builder"]["target_version"]!="1.5.0":
        errors.append("target builder version must be 1.5.0")
    if contract["builder"]["behavior_preserving"] is not True:
        errors.append("migration must remain behavior-preserving")
    if canonical!=legacy:
        errors.append("canonical instruction diverges from legacy instruction")
    if version!="1.0.0":
        errors.append(f"VERSION changed during migration: {version!r}")

    if len(list((ROOT/"knowledge").glob("*.md")))!=9:
        errors.append("expected exactly 9 Knowledge files")
    if len(list((ROOT/"templates").glob("*.md")))!=5:
        errors.append("expected exactly 5 template files")
    if len(list((ROOT/"examples").glob("*.md")))!=3:
        errors.append("expected exactly 3 example files")

    markers=[
        "ställ högst 3 följdfrågor åt gången",
        "Återge inte långa bibelavsnitt från moderna upphovsrättsskyddade översättningar.",
        "Skilj alltid mellan bibeltext, historisk bakgrund, språkliga observationer, teologisk tolkning och praktisk tillämpning.",
        "Standard: ekumeniskt och balanserat.",
        "När tolkningar skiljer sig:",
        "Skapa tydlig Markdown med konsekventa rubriker, listor och länkar.",
    ]
    for marker in markers:
        if marker not in text:
            errors.append(f"canonical instruction missing behavior marker: {marker}")

    b=contract["behavior"]
    if b.get("dialog_driven_start") is not True:
        errors.append("dialog_driven_start must be true")
    if b.get("max_followup_questions_per_turn")!=3:
        errors.append("max_followup_questions_per_turn must remain 3")
    if b.get("reference_plus_link_default") is not True:
        errors.append("reference_plus_link_default must be true")
    if b.get("default_theological_profile")!="ecumenically_balanced":
        errors.append("default theological profile changed")
    if b.get("markdown_default_for_export_material") is not True:
        errors.append("Markdown export default changed")
    if len(b.get("study_modes",[]))!=6:
        errors.append("expected six preserved study modes")

    if errors:
        print("GPT BUILDER 1.5 CONTRACT: FAIL")
        for e in errors: print("-",e)
        return 1
    print("GPT BUILDER 1.5 CONTRACT: PASS")
    print("VERSION 1.0.0; 9 Knowledge; 5 templates; 3 examples; dialog/source/theology/output behavior preserved")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
