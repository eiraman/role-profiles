# Formato di `eiraman/stato.json`

Il Coordinatore AI mantiene `eiraman/stato.json` come **istantanea strutturata** del progetto. La Vista del Manager (`tools/vista_manager.py`) la legge e genera `eiraman/vista/index.html`, con l'albero dei Work Package, e `eiraman/vista/documenti.html`, con i documenti di progetto del Manager umano. I file narrativi restano la fonte di dettaglio: `mandato.md`, `decisioni.md`, `piano.md` e `registro.jsonl`. `stato.json` li riassume per il Manager umano.

Il Coordinatore AI aggiorna `stato.json` e rigenera la vista:
- all'apertura del progetto;
- quando nasce o si chiude un Do;
- quando si supera una soglia di budget;
- alla chiusura di una Wave;
- alla revisione del ciclo di governo;
- quando cambia l'avanzamento di un Work Package in corso, almeno una volta al giorno di lavoro.

Ogni dato numerico ha la sua fonte nel registro. Se non è misurato, si indica «sconosciuto»: non si scrive mai zero.

```json
{
  "lingua": "it",
  "progetto": "Nome del progetto",
  "visione": "Una frase: problema, utenti, beneficio",
  "metodo": "The Eiraman Guide 1.0.0-rc.6",
  "modalita": "bloccante | informativa",
  "classe": 0,
  "livello": 0,
  "security_report": {"percorso": "security-report.md", "aggiornato": "2026-11-25"},
  "fase": "Scoperta | POC | Design e planning | Scale | Accettazione ed esercizio",
  "aggiornato": "2026-11-25T10:00:00Z",
  "ciclo": {"numero": 1, "inizio": "2026-11-24", "revisione": "2026-11-28",
            "quota_governo": {"governo": 3.2, "totale": 12.5},
            "fuori_catalogo": {"task": 2, "totale": 31}},
  "budget": {"valuta": "EUR", "tetto": 100, "speso": 12.5, "sconosciuto": 3,
             "nota": "3 esecuzioni in abbonamento senza importo"},
  "cattive_notizie": ["Una prova è fallita ed è stata ripetuta.", "…"],
  "decisioni": [
    {"id": "Do-04", "titolo": "Scelta dello stack", "domanda": "Quale opzione approvi?",
     "opzioni": [{"nome": "A", "effetto": "costi, tempi, funzioni"}, {"nome": "B", "effetto": "…"}],
     "raccomandazione": "A, perché …", "scadenza": "2026-11-27",
     "se_non_rispondi": "Il pacchetto resta sospeso; il lavoro indipendente prosegue.",
     "stato": "aperto | deciso | scaduto", "esito": ""}
  ],
  "pacchetti": [
    {"id": "WP-W1-01", "titolo": "…", "wave": "W1",
     "fase": "Scoperta | POC | Design e planning | Scale | Accettazione ed esercizio",
     "avanzamento": "completato | in corso | da fare",
     "controlli": {"superati": 4, "totale": 10},
     "stima_costo": 18, "costo_effettivo": 20.5,
     "descrizione": "Che cosa produce, in linguaggio di business",
     "deliverable": ["Pagina elenco", "Prova di accettazione"],
     "squad": [{"ruolo": "Sviluppatore", "profilo": "sviluppatore-web 0.2.0",
                "modello": "nome esatto del modello", "ragionamento": "medio"}],
     "tecnico": "aperto | chiuso su prova | sospeso",
     "accettazione": "da fare | accettato | rifiutato",
     "pubblicazione": "no | sì", "evidenza": "percorso relativo o descrizione"}
  ],
  "documenti": [
    {"titolo": "High Level Architectural View", "percorso": "architettura.md",
     "livello": "strategico | manageriale", "nota": "facoltativa"}
  ],
  "consegne": ["Funzione X accettata con prova."],
  "prossimo_ciclo": "Che cosa propone il Coordinatore AI per il ciclo successivo."
}
```

**Modalità e Security Report** (Guida §14, «Classification mode», «Security Officer in the informative mode»). `modalita` è la modalità della classificazione registrata all'apertura: `bloccante` o `informativa`. La vista la mostra in testa; se manca, scrive «non registrata» e lo aggiunge alle cattive notizie. In modalità informativa `classe` resta `null` (convenzione del profilo del Coordinatore AI, §5 bis) e la vista, al posto della classe, rimanda al Security Report. `security_report` indica la copia immutata del report corrente, con percorso relativo a `eiraman/` (di default `security-report.md`) e la data dell'ultimo aggiornamento: la vista la collega in testa e fra i documenti manageriali. In modalità informativa, se il report manca, la vista lo aggiunge alle cattive notizie come documento dovuto e non prodotto. In modalità bloccante il campo non serve.

**Albero dei Work Package.** L'albero raggruppa i pacchetti per Wave e mostra sui rami la `stima_costo`, nella valuta del budget. `controlli` vale solo per i pacchetti in corso: indica i controlli obbligatori della scheda del Work Package superati sulla candidata e il loro totale, e la vista li mostra come «4/10» (regola del denominatore, Guida §12, «Percentages»). Il campo `percentuale` delle versioni precedenti non dichiara il denominatore e non viene più mostrato: va sostituito con `controlli`. Un pacchetto in corso senza `controlli` compare con «?» e con la dicitura «avanzamento non dichiarato». Un pacchetto senza `avanzamento` è «completato» se lo stato tecnico è «chiuso su prova», altrimenti «da fare». Una stima assente compare come «?».

**Documenti di progetto.** `documenti` elenca i soli documenti strategici e manageriali, con percorsi relativi alla cartella `eiraman/`. Il generatore li converte da Markdown in pagine leggibili. Se `documenti` manca, cerca mandato.md, architettura.md (High Level Architectural View), piano.md, decisioni.md, rischi.md, executive.md, performance.md, in modalità informativa il Security Report (`security_report`, di default security-report.md), e le revisioni in `ciclo/`. Se `documenti` c'è e non elenca il Security Report, in modalità informativa la vista lo aggiunge. Non pubblica mai `registro.jsonl`, `stato.json`, le evidenze né la cartella `vista/`, anche con maiuscole diverse, e rifiuta percorsi fuori da `eiraman/`: un documento rifiutato compare come «non mostrato». Collegamenti e immagini nei documenti sono relativi alla cartella `eiraman/` e seguono le stesse regole; un disegno si include con `![testo](architettura.svg)`.

**Fase dei pacchetti.** Ogni pacchetto dichiara in `fase` la fase a cui appartiene. In `avanzamento` valgono «completato» e «da fare»; ogni altro valore (in corso, da rivedere, sospeso, consegnato) conta come lavoro avviato e non chiuso. La vista usa i due campi per un controllo e aggiunge da sola, fra le cattive notizie:
- che il lavoro di costruzione è partito con una fase non chiusa, se un pacchetto di una fase successiva è avviato o completato mentre i pacchetti di Scoperta, o quelli di Design e planning, mancano o non sono tutti completati;
- che la fase non è dichiarata, se un pacchetto avviato o completato non ha `fase` o ne ha una che la vista non riconosce.

Il controllo legge ciò che il Coordinatore AI scrive in `stato.json`: non vede un pacchetto di costruzione dichiarato con la fase sbagliata, né un elenco di pacchetti vuoto, né un pacchetto senza `avanzamento` il cui stato tecnico non è «chiuso su prova», che conta come «da fare». Gli avvisi automatici compaiono dopo le cattive notizie scritte dal Coordinatore AI. Non sostituisce il Revisore AI, che verifica il controllo delle fasi sulle evidenze.

**Quote del ciclo.** `ciclo.quota_governo` riporta il costo di governo del ciclo e il costo totale, nella valuta del budget: sono di governo i run del Coordinatore AI, degli AI Scrum Master, dei revisori, del classificatore di escalation (E4), dei giudici (K1), del gate di applicabilità e della redazione dei documenti manageriali (Guida §8, «Governance cycle»; §11, «Run traceability»). `ciclo.fuori_catalogo` riporta i task eseguiti fuori catalogo e il totale dei task del ciclo (Guida §7.1, «Fallback»). La vista mostra le due quote con numeratore e denominatore; se un campo manca, scrive «sconosciuta», mai zero.

Campi facoltativi: `rischi` (elenco di frasi), `escalation_ciclo` (numero di Do del ciclo), `indicatore_do` (valore di riferimento dichiarato nel mandato, di default 3).

Il generatore aggiunge da solo alle cattive notizie le decisioni scadute o incomplete e il superamento dell'80% o del 100% del budget. Se la spesa non è misurata, la barra resta neutra e la pagina dice che il tetto non è verificabile.
