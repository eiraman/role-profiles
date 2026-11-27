# Istruzioni per gli autori: catalogo dei task (Seniority Digitale)

Leggi `_seniority/SENIORITY.md` e `_seniority/seniority.json`. Poi, per ogni profilo della tua famiglia, nel solo `profilo.json`:

1. Aggiungi `"seniority": {"minima": "SDx", "massima": "SDy", "nota": "…"}`: l'intervallo tipico del ruolo.
2. Aggiungi `"catalogo"`: da 6 a 12 voci `{"id": "T01", "task": "…", "deliverable": "…", "seniority": "SDn", "note": "…"}`. Le ricavi dalle sezioni 3 e 4 del PROFILO.md e dalla vecchia `matrice_compiti`. Ogni task è un lavoro che il Coordinatore AI può assegnare, con il deliverable concreto che produce.
3. Assegna il livello come in un'organizzazione umana: il livello **minimo** con cui il task si esegue bene.
   - **SD1** solo per compiti ripetitivi con esito verificabile da un controllo deterministico.
   - **SD2** per il lavoro corrente su specifica chiara.
   - **SD3** per diagnosi, revisione e scelte locali.
   - **SD4** per architettura, sicurezza, effetti difficili da annullare, schede Do e giudizi.
   - **SD5** solo per eccezione motivata nella nota.
   - Un task di verifica indipendente sta almeno al livello del lavoro che verifica.
4. Elimina `matrice_compiti`. Non toccare `motori`, `unit_cost` e `mode_role`: li normalizza il Coordinatore AI con uno script.
5. Non scrivere a mano la sezione 10 di PROFILO.md. Esegui `python3 -I _strumenti/attiva_profilo.py --scrivi-catalogo <cartelle>`. Poi, nella sezione 1 di PROFILO.md, aggiungi una riga: «Seniority Digitale: vedi sezione 10; un task fuori catalogo si esegue al livello di ripiego fissato nel mandato, con i valori indicativi della sezione 10 (Guida 1.0.0-rc.6, §7.1, «Fallback»).»
6. Valida con `python3 -I _strumenti/valida_profilo.py <cartelle>` finché non esce OK. Gli errori sui campi `motori` o `unit_cost` riportali, ma non correggerli.
