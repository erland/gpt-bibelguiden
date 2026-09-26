# GPT Byggaren 1.5.0 – migreringsplan

Projekt: **Bibelguiden**

## Preserve-first baseline

Migreringen ska bevara:
- version **1.0.0**
- exakt **9 Knowledge-filer**
- exakt **5 templates**
- exakt **3 exempel**
- `gpt/instructions.md` byte-identiskt som canonical beteendekälla
- dialogdriven start med högst 3 följdfrågor åt gången
- studielägena smågrupp, självstudie, bibelstudiebok, ledarguide, ungdom/familj och transformering
- referens + länk som standard framför längre återgivning av moderna bibelöversättningar
- tydlig åtskillnad mellan bibeltext, historisk bakgrund, språkliga observationer, teologisk tolkning och praktisk tillämpning
- ekumeniskt balanserad teologisk profil som standard
- transparens när kristna traditioner tolkar olika
- Markdown som standard för exportmaterial
- befintliga Chat- och Custom GPT-distributioner

## Steg

1. Etablera canonical instruktion och projektkontrakt.
2. Normalisera capability-, artifact-, workspace/state- och tool-kontrakt.
3. Normalisera Chat och Custom GPT till samma canonical källa.
4. Bedöm Claude Projects och OpenCode.
5. Bedöm OpenAI Plugin.
6. Generalisera build, parity, CI och release via runtime-registry.
7. Slutlig readiness, dokumentationssynk och 7/7-gate.

## Aktivering av nya runtimes

En runtime får bara aktiveras om den kan bevara käll-/citatpolicyn, teologisk balans, dialogdriven behovsanalys, studielägen och strukturerat Markdown-material utan kritisk degradering.
