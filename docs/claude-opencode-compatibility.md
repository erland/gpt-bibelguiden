# Claude Projects och OpenCode – runtime compatibility

Projekt: **Bibelguiden**  
GPT Byggaren: **1.5.0**

## Slutsats

Både Claude Projects och OpenCode bedöms som **equivalent candidates** på kontraktsnivå, men lämnas **inte aktiva** i denna migrering.

Bibelguidens kärna består av instruktioner, Knowledge, templates, exempel, dialogdriven behovsanalys och strukturerade Markdown-artefakter. Det finns ingen unik media- eller exekveringscapability som i sig blockerar parity.

Aktivering kräver ändå en faktisk distribution/adapterspecifikation och regressionstester som verifierar käll-/citatpolicy, teologisk balans, dialogbeteende, studielägen och exportformat.

## Parity-bedömning

| Område | Claude Projects | OpenCode |
|---|---|---|
| Behavior | equivalent candidate | equivalent candidate |
| Capability | equivalent candidate | equivalent candidate |
| Artifact | equivalent candidate | equivalent candidate |
| Workspace/state | equivalent candidate | equivalent candidate |
| Tool | equivalent candidate | equivalent candidate |

## Kritiska regler som måste bevaras

Varje runtime måste bevara:
- dialogdriven start,
- högst tre följdfrågor åt gången,
- referens + länk framför längre moderna bibelcitat,
- tydlig åtskillnad mellan bibeltext, historisk bakgrund, språkliga observationer, teologisk tolkning och praktisk tillämpning,
- ekumeniskt balanserad standardprofil,
- transparens när kristna traditioner tolkar olika,
- samtliga sex studielägen,
- Markdown som standard för exportmaterial,
- 9/9 Knowledge-filer,
- 5/5 templates,
- 3/3 exempel.

## Claude Projects

Beslut:
- compatibility: `equivalent`
- activation: `not_active`
- blocker: `distribution_and_regression_not_implemented`

## OpenCode

Beslut:
- compatibility: `equivalent`
- activation: `not_active`
- blocker: `distribution_and_regression_not_implemented`

## Aktiveringsregel

En runtime får aktiveras först när:
1. canonical instruktion paketeras deterministiskt,
2. Knowledge/templates/examples inkluderas eller representeras verifierat equivalent,
3. käll-/citatpolicyn regressionstestas,
4. teologisk balans och perspektivhantering verifieras,
5. dialogstart och studielägen verifieras,
6. Markdown-output och transformering verifieras,
7. distributionen byggs och valideras i CI.

Ingen canonical produktregel ändras av denna bedömning.
