# Bibelguiden GPT – startpaket v4

Detta paket innehåller material för att skapa en egen GPT för bibelstudier, smågrupper, självstudier och tematiska bibelstudieböcker.

## Viktigt i v4
- `gpt/instructions.md` är komprimerad till under 8000 tecken.
- `knowledge/` innehåller 8 filer, alltså väl under GPT Builder-gränsen på 20 Knowledge-filer.
- Smågrupp, självstudie, studiebok och transformering stöds som separata arbetslägen.

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
