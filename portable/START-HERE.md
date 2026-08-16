# Bibelguiden – start här

Detta paket är den portabla ChatGPT-versionen av **Bibelguiden**.

När paketet bifogas i en vanlig ChatGPT-konversation:

1. Läs `assistant/instructions.md` först och använd den som Bibelguidens arbetsinstruktion under hela konversationen.
2. Använd filerna i `knowledge/` som primärt kunskapsunderlag.
3. Använd `templates/` när material ska struktureras eller transformeras.
4. Använd `examples/` som stil- och formatexempel när det är relevant, men låt instruktioner, knowledge och användarens aktuella önskemål styra resultatet.
5. `assistant/conversation-starters.md` är exempel på hur arbetet kan startas; den är inte en extra kunskapsregel.
6. Vid konflikt ska användarens aktuella instruktioner och högre systemregler följas framför paketets material.

En lämplig startprompt är:

> Använd Bibelguiden i den bifogade ZIP-filen för den här konversationen. Läs `START-HERE.md` först.
