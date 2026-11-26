# Avviare il Coordinatore AI Eiraman

**Prima di iniziare.** Se hai scaricato il kit come zip, confronta l'impronta SHA-256 del file con quella pubblicata nel prompt di avvio su <https://eiraman.tech/come-usarlo.html> (in inglese: <https://eiraman.tech/en/how-to-use.html>). Per calcolarla: `shasum -a 256 eiraman-kit.zip` su macOS e Linux, `Get-FileHash eiraman-kit.zip -Algorithm SHA256` in PowerShell su Windows. Se non coincide, non usare il kit.

**Stato.** Nel kit attuale i divieti del mandato sono istruzioni seguite dal Coordinatore AI, non ancora un blocco tecnico dell'ambiente.

1. Crea o apri la cartella del progetto applicativo.
2. Copia nella cartella:
   - `CONTROLLORE.md` e `STATO.md`;
   - `tools/vista_manager.py`, il generatore della Vista del Manager;
   - la specifica, come `framework/Eiraman.md`.
3. Apri una sessione di **Claude Code** o di **Codex** in quella cartella.
4. Incolla questo messaggio, sostituendo la parte tra parentesi:

```text
Leggi CONTROLLORE.md e framework/Eiraman.md. Da ora sei il Coordinatore AI Eiraman di questo progetto e io sono il Manager umano. Segui la procedura di avvio del profilo e apri la Vista del Manager. [Visione, se già disponibile: problema, utenti, beneficio atteso.]
```

Per far partire il Coordinatore AI in automatico, rinomina o collega `CONTROLLORE.md` come istruzioni permanenti della cartella:
- **Claude Code:** `CLAUDE.md`, che può contenere solo la riga `@CONTROLLORE.md`;
- **Codex:** `AGENTS.md`.

**Revisore AI.** Prima della prima Wave il Coordinatore AI prepara l'ambiente del Revisore AI (profilo `governo/revisore-ai`), che lavora in una sessione separata, con i soli file del suo ruolo e, dove disponibile, su un modello diverso da quello del Coordinatore AI. Se per avviarlo serve una tua azione, per esempio aprire una sessione con un altro fornitore, il Coordinatore AI te la chiede.

Per riprendere un progetto, apri una nuova sessione nella stessa cartella e scrivi: «Riprendi come Coordinatore AI Eiraman». Il registro in `eiraman/` conserva lo stato.

Durante l'esecuzione il Coordinatore AI apre la **Vista del Manager** (`eiraman/vista/index.html`) nel pannello del browser di Claude Code o, in Codex, con il comando di apertura del sistema. Tienila aperta: è il tuo cruscotto per le decisioni, il budget e lo stato del lavoro.
