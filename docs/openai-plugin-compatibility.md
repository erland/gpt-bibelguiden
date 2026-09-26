# OpenAI Plugin – compatibility assessment

Projekt: **Bibelguiden**  
GPT Byggaren: **1.5.0**

## Slutsats

OpenAI Plugin bedöms som **equivalent candidate**, **skills-first** och lämnas **inte aktiv** i denna migrering.

Bibelguidens kärna består av instruktioner, Knowledge, templates, exempel, dialogdriven behovsanalys och strukturerad Markdown. Det finns ingen unik runtime-capability som i sig blockerar parity.

Aktivering kräver däremot en faktisk plugin-distribution med skills som bevarar käll-/citatpolicy, teologisk balans, studielägen, templates och outputkontrakt samt automatiska regressionstester.

## Parity-bedömning

| Område | Bedömning |
|---|---|
| Behavior | equivalent candidate |
| Capability | equivalent candidate |
| Artifact | equivalent candidate |
| Workspace/state | equivalent candidate |
| Tool | equivalent candidate |

## Skills-first upplägg

En framtida Plugin v1 bör minst ha skills för:
- dialogdriven studiedesign,
- val av studieläge och målgrupp,
- bibelreferenser och länkpolicy,
- teologisk balans och perspektivhantering,
- översättningsnoteringar och parallelltexter,
- smågruppsmaterial,
- självstudie,
- bibelstudiebok,
- ledarguide,
- ungdom/familj,
- transformering mellan studieformat,
- strukturerad Markdown-export.

Knowledge, templates och exempel måste inkluderas direkt eller representeras på ett verifierat equivalent sätt.

## Kritiska regler som måste regressionstestas

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

## Aktiveringsbeslut

- status: `assessed_not_active`
- compatibility: `equivalent`
- architecture: `skills_first`
- activation: `not_active`
- blocker: `plugin_distribution_and_regression_not_implemented`

Ingen Plugin-distribution byggs eller publiceras i denna migrering.

## Aktiveringsregel

Plugin får aktiveras först när:
1. skills-strukturen är implementerad,
2. canonical instruktion och Knowledge/templates/examples representeras deterministiskt,
3. käll-/citatpolicyn regressionstestas,
4. teologisk balans och perspektivhantering verifieras,
5. dialogstart och studielägen verifieras,
6. Markdown-output och transformering verifieras,
7. plugin-distributionen byggs och valideras i CI.

Ingen canonical produktregel ändras av denna bedömning.
