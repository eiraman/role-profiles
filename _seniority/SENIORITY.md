# Seniority Digitale

In un'organizzazione ogni persona lavora al livello di esperienza che il compito richiede: non si chiede a un principal di formattare una tabella, né a un junior di disegnare un'architettura. Eiraman applica la stessa regola agli agenti. La **Seniority Digitale** di un agente è la combinazione di **motore** (per esempio Haiku, Sonnet, Opus, Fable) e **livello di ragionamento** (effort) con cui il Coordinatore AI lo attiva.

| Livello | Nome | Quando | Claude Code | Codex | GitHub Copilot |
|---|---|---|---|---|---|
| SD1 | Junior | Compiti ripetitivi con esito verificabile da un controllo deterministico | `model: haiku`, `effort: low` | `gpt-6-luna`, `low` | Claude Haiku 5.5 |
| SD2 | Professional | Lavoro corrente su specifica chiara | `model: sonnet`, `effort: medium` | `gpt-6.2-sol`, `medium` | Claude Sonnet 5.5 |
| SD3 | Senior | Scelte locali di progetto, diagnosi, revisione | `model: sonnet`, `effort: high` | `gpt-6.2-sol`, `high` | Claude Sonnet 5.5 |
| SD4 | Lead | Architettura, sicurezza, effetti difficili da annullare, schede Do, giudizio; **ripiego per ogni compito fuori catalogo** | `model: opus`, `effort: high` | `gpt-6.2-astra`, `high` | Claude Opus 5.5 |
| SD5 | Principal | Problemi nuovi o ad alto impatto, per eccezione e con motivazione | `model: fable`, `effort: xhigh` | `gpt-6.2-astra`, `xhigh` | Claude Fable 5.2 |

**Regole.**
1. Ogni Role Profile contiene il **catalogo** dei task e dei deliverable che il Coordinatore AI può assegnargli, ciascuno con il livello minimo. La configurazione di ogni riga deriva da questa tabella (`seniority.json`).
2. **Ripiego.** Un task che non rientra nel catalogo si esegue a **SD4**. Il Coordinatore AI lo registra e propone di aggiungerlo al catalogo (ritorno al metodo, spec §11).
3. **Squadra.** Un agente partecipa a uno Scrum Team con la seniority **più alta** richiesta dai task che deve eseguire nel Work Package.
4. **Verifica.** Il revisore o tester indipendente lavora almeno allo stesso livello dell'esecutore che verifica.
5. **Ritocchi.** Dopo due tentativi falliti per carenza di capacità, il Coordinatore AI sale di un livello e lo registra. La promozione usa i tentativi consentiti dalla scheda del Work Package: se sono esauriti, apre un punto decisionale. SD5 richiede una motivazione registrata. Nella retrospettiva può proporre di abbassare il livello di un task del catalogo se le prove mostrano qualità invariata a costo minore. È una porta a due vie entro la tolleranza del mandato: oltre la tolleranza è un Do.
6. **Costo.** Lo Unit Cost si tara per livello: la stessa attività costa diversamente a SD2 e a SD4.
7. Le configurazioni si **riverificano a ogni cambio di modello**. Un nome di modello non più disponibile si sostituisce con il più vicino dello stesso livello, e il cambio si registra.
