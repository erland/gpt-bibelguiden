# Bibelguiden GPT – startpaket v4-dialog

Detta paket innehåller material för att skapa en egen GPT för bibelstudier, smågrupper, självstudier och tematiska bibelstudieböcker.

## Viktigt i v4
- `gpt/instructions.md` är komprimerad till under 8000 tecken.
- `knowledge/` innehåller 9 filer, alltså väl under GPT Builder-gränsen på 20 Knowledge-filer.
- Smågrupp, självstudie, studiebok och transformering stöds som separata arbetslägen. Denna justerade version har dessutom dialogdriven start där användaren kan börja mycket generellt och GPT:n hjälper till att välja inriktning.

## Rekommenderad användning i GPT Builder
1. Skapa en ny GPT.
2. Namn: **Bibelguiden**.
3. Beskrivning: använd texten i `gpt/gpt-builder-config.md`.
4. Instructions: kopiera allt från `gpt/instructions.md`.
5. Conversation starters: kopiera relevanta rader från `gpt/conversation-starters.md`.
6. Knowledge: ladda upp filerna i `knowledge/` och gärna `templates/`.

## Innehåll
- `gpt/` – instruktioner och GPT Builder-material
- `knowledge/` – policyer, regler och pedagogiska riktlinjer
- `templates/` – mallar för smågrupp, självstudie, studiebok och transformering
- `examples/` – exempelmaterial
- `docs/` – skaparanteckningar

## Rekommenderad designprincip
Bibelguiden ska inte återpublicera längre bibeltexter från moderna översättningar. Den ska i första hand ge referenser och direktlänkar till rätt bibeltext, och sedan hjälpa med frågor, kontext, samband, fördjupning och praktisk tillämpning.


## Nytt i v4-dialog
- Bygger på den bifogade v4-versionen.
- Lägger till dialogdriven behovsanalys före materialproduktion.
- Stödjer generella startfrågor där GPT:n ger förslag och ställer få följdfrågor åt gången.
- Behåller v4:s mallar, exempel och knowledge-struktur.

## Distributionspaket

Repositoryt kan bygga två distributionsformer från samma källfiler:

- **Custom GPT** – installationspaket för GPT Builder med nuvarande instruktioner, Knowledge, mallar och exempel oförändrade.
- **Portable Chat** – ZIP som kan bifogas i en vanlig ChatGPT-konversation och startas via `START-HERE.md`.

Bygg lokalt:

```bash
python3 scripts/build_distributions.py
python3 scripts/validate_distributions.py
```

Vanliga push-, pull request- och manuella workflow-körningar använder versionsnumret i `VERSION`. När en GitHub Release publiceras används release-taggen som versionskälla. En release med taggen `v1.1.0` skapar därför:

```text
bibelguiden-custom-gpt-v1.1.0.zip
bibelguiden-chat-v1.1.0.zip
```

Release-paketen bifogas automatiskt som assets till GitHub Release och bevaras där för framtida nedladdning.
