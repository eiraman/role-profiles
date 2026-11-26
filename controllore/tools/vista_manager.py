#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 Paolo Ungari and contributors
# SPDX-License-Identifier: Apache-2.0
# Earlier copies distributed up to version 0.3.x under the MIT licence remain available under that licence.
"""Vista del Manager · Eiraman

Legge eiraman/stato.json (e, se presente, eiraman/registro.jsonl) e genera
eiraman/vista/index.html: una pagina autonoma, senza rete né dipendenze,
che il Coordinatore AI fa aprire al Manager umano nel pannello del browser
di Claude Code o di Codex.

Uso:  python3 tools/vista_manager.py [cartella_progetto]
Stampa il percorso assoluto della pagina generata.
"""
import html, json, os, sys
from datetime import date, datetime

L = {
 "it": dict(title="Vista del Manager", proj="Progetto", phase="Fase", cls="Classe", lvl="Livello", cycle="Ciclo",
   review="revisione", updated="Aggiornato", bad="Prima le cattive notizie", none_bad="Nessuna cattiva notizia registrata.",
   dos="Decisioni per te", none_do="Nessuna decisione in attesa.", deadline="Scadenza", rec="Raccomandazione",
   ifnot="Se non rispondi", options="Opzioni", decided="Decise", budget="Budget", spent="speso", cap="tetto",
   unknown="esecuzioni senza importo misurato", alert80="Avviso: superato l'80% del tetto.", block100="Tetto raggiunto: nessun nuovo lavoro.",
   pk="Pacchetti di lavoro", tech="Stato tecnico", acc="Accettazione", pub="Pubblicazione", ev="Evidenza",
   deliv="Consegnato in questo ciclo", next="Proposta per il ciclo successivo", risks="Rischi", vision="Visione",
   missing="mancante", nav_view="Vista", nav_docs="Documenti di progetto", docs_title="Documenti di progetto", docs_hint="Documenti strategici e manageriali del progetto. I documenti tecnici restano agli agenti.", strategic="Strategici", managerial="Manageriali", absent="non ancora prodotto", refused="non mostrato: percorso non ammesso", back="Torna ai documenti", d_mandato="Mandato", d_decisioni="Registro delle decisioni", d_piano="High Level Plan", d_arch="High Level Architectural View", d_rischi="Risk Log", d_exec="Executive Description", d_perf="Performance Analysis", d_ciclo="Revisione del ciclo", tree="Albero del progetto", tree_hint="Clicca un Work Package per vederne deliverable e squad. Sui rami: stima di costo per eseguirlo.", done_s="completato", prog_s="in corso", todo_s="da fare", est="Stima", actual="Costo effettivo", deliverable="Deliverable", squad="AI Squad", role="Ruolo", profile="Role Profile", model="Modello", reasoning="Ragionamento", desc="Descrizione", progress="Avanzamento", legend_done="Completati", legend_prog="In corso, con i controlli obbligatori superati sul totale", checks="controlli obbligatori superati", gov_share="Quota di governo", off_cat="Task fuori catalogo", of="su", unk="sconosciuta", no_den="avanzamento non dichiarato: mancano i controlli superati e il totale", auto_phase="Lavoro di costruzione avviato con una fase non chiusa", ph_disc="Scoperta", ph_design="Design e planning", auto_nophase="Pacchetti in corso o completati senza la fase dichiarata: non si può verificare che Scoperta e Design e planning siano chiusi.", legend_todo="Da fare", unknown_spend="Spesa non misurata: il tetto non è verificabile.", auto_late="Decisione scaduta senza risposta", auto_80="La spesa ha superato l'80% del tetto.", auto_100="La spesa ha raggiunto il tetto: nessun nuovo lavoro.", auto_missing="Decisione incompleta (mancano scadenza o effetto della mancata risposta)",
   foot="Pagina generata dal Coordinatore AI dal registro del progetto. Per rispondere a una decisione scrivi nella chat della sessione.",
   rp_title="Role Profile attivati dal Coordinatore", rp_hint="I ruoli AI che il Coordinatore ha attivato per eseguire il progetto, con il motore usato e il lavoro svolto.", rp_qual="Qualificazione", rp_tasks="Compiti", rp_wp="Work Package", rp_runs="Esecuzioni", rp_none="Nessun Role Profile registrato.",
   expired="scaduta", today="oggi", days="giorni", do_count="Do in questo ciclo", ref="riferimento", runs="Esecuzioni registrate", no_reg="Registro delle esecuzioni non presente."),
 "en": dict(title="Manager view", proj="Project", phase="Phase", cls="Class", lvl="Level", cycle="Cycle",
   review="review", updated="Updated", bad="Bad news first", none_bad="No bad news recorded.",
   dos="Decisions for you", none_do="No decision pending.", deadline="Deadline", rec="Recommendation",
   ifnot="If you do not answer", options="Options", decided="Decided", budget="Budget", spent="spent", cap="cap",
   unknown="runs with no measured amount", alert80="Warning: over 80% of the cap.", block100="Cap reached: no new work.",
   pk="Work packages", tech="Technical state", acc="Acceptance", pub="Publication", ev="Evidence",
   deliv="Delivered this cycle", next="Proposal for the next cycle", risks="Risks", vision="Vision",
   missing="missing", nav_view="View", nav_docs="Project documents", docs_title="Project documents", docs_hint="Strategic and managerial documents of the project. Technical documents stay with the agents.", strategic="Strategic", managerial="Managerial", absent="not produced yet", refused="not shown: path not allowed", back="Back to documents", d_mandato="Mandate", d_decisioni="Decision log", d_piano="High Level Plan", d_arch="High Level Architectural View", d_rischi="Risk Log", d_exec="Executive Description", d_perf="Performance Analysis", d_ciclo="Cycle review", tree="Project tree", tree_hint="Click a Work Package to see its deliverables and squad. On the branches: estimated cost to run it.", done_s="completed", prog_s="in progress", todo_s="to do", est="Estimate", actual="Actual cost", deliverable="Deliverables", squad="AI Squad", role="Role", profile="Role Profile", model="Model", reasoning="Reasoning", desc="Description", progress="Progress", legend_done="Completed", legend_prog="In progress, with mandatory checks passed over the total", checks="mandatory checks passed", gov_share="Governance share", off_cat="Tasks outside the catalogue", of="of", unk="unknown", no_den="progress not declared: checks passed and total are missing", auto_phase="Build work started with a phase not closed", ph_disc="Discovery", ph_design="Design and planning", auto_nophase="Packages in progress or completed without a declared phase: it cannot be checked that Discovery and Design and planning are closed.", legend_todo="To do", unknown_spend="Spend not measured: the cap cannot be checked.", auto_late="Decision overdue without an answer", auto_80="Spend is over 80% of the cap.", auto_100="Spend has reached the cap: no new work.", auto_missing="Incomplete decision (deadline or effect of no answer missing)",
   foot="Page generated by the AI Coordinator from the project registry. To answer a decision, write in the session chat.",
   rp_title="Role Profiles activated by the Coordinator", rp_hint="The AI roles the Coordinator activated to run the project, with the engine used and the work done.", rp_qual="Qualification", rp_tasks="Tasks", rp_wp="Work Packages", rp_runs="Runs", rp_none="No Role Profile recorded.",
   expired="overdue", today="today", days="days", do_count="Do this cycle", ref="reference", runs="Recorded runs", no_reg="No run log available."),
}

import re as _re
_CTRL = _re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]")
def e(x):
    if x is None: return ""
    if isinstance(x, (dict, list)): x = json.dumps(x, ensure_ascii=False)
    return html.escape(_CTRL.sub("", str(x)))

def as_list(x):
    if x is None: return []
    if isinstance(x, list): return x
    return [x]

def as_dict(x, key="titolo"):
    if isinstance(x, dict): return x
    return {key: x}

def days_left(s):
    try:
        d = datetime.fromisoformat(str(s)[:10]).date()
        return (d - date.today()).days
    except Exception:
        return None

def money(v, cur):
    if v is None or v == "":
        return "?"
    try:
        return f"{float(v):,.2f} {cur}".replace(",", " ")
    except Exception:
        return str(v)


def _slug(x):
    return "wp-" + (_re.sub(r"[^A-Za-z0-9_-]+", "-", str(x)).strip("-") or "x")

def _short(x, n):
    x = str(x or "")
    return x if len(x) <= n else x[:n - 1] + "…"

def _checks(p):
    """Controlli obbligatori superati e totale di un pacchetto in corso, oppure None se non dichiarati."""
    c = p.get("controlli")
    try:
        sup, tot = int(c["superati"]), int(c["totale"])
        return (max(0, min(sup, tot)), tot) if tot > 0 else None
    except Exception:
        return None

def _prog_label(p, pc):
    """Avanzamento con il denominatore: «4/10»; «?» se i controlli non sono dichiarati."""
    c = _checks(p)
    return f"{c[0]}/{c[1]}" if c else "?"

def _share(d, num, den, t, cur=None):
    """«X su Y (Z%)» da un dizionario {num, den}; «sconosciuta» se manca o non è misurata."""
    try:
        a, b = float(d[num]), float(d[den])
        if b <= 0: return t["unk"]
        fa, fb = (money(a, cur), money(b, cur)) if cur else (f"{a:g}", f"{b:g}")
        return f"{fa} {t['of']} {fb} ({100.0 * a / b:.0f}%)"
    except Exception:
        return t["unk"]

def _status(p):
    a = str(p.get("avanzamento") or "").strip().lower()
    if a in ("completato", "completed", "done", "chiuso"): return "done", 100
    if a in ("da fare", "to do", "todo"): return "todo", 0
    if a in ("in corso", "in progress", "doing", "attivo"):
        c = _checks(p)  # il vecchio campo `percentuale` non dichiara il denominatore: non si mostra
        return "prog", (int(round(100.0 * c[0] / c[1])) if c else None)
    tec = " ".join(str(p.get("tecnico") or "").lower().split())
    if tec in ("chiuso su prova", "closed on evidence"): return "done", 100
    return "todo", 0

_PHASES = {"scoperta": 0, "discovery": 0, "poc": 1, "design e planning": 2, "design and planning": 2,
           "scale": 3, "accettazione ed esercizio": 4, "acceptance and operation": 4}

def phase_alerts(s, t):
    """Cattive notizie automatiche: pacchetti di costruzione avviati con Scoperta o Design e planning non chiusi."""
    pk = [as_dict(x) for x in as_list(s.get("pacchetti"))]
    active = [p for p in pk if _status(p)[0] in ("prog", "done")]
    if not active: return []
    def ph(p): return _PHASES.get(" ".join(str(p.get("fase") or "").lower().split()))
    if any(ph(p) is None for p in active): return [t["auto_nophase"]]
    out = []
    for need, later in ((0, 1), (2, 3)):
        closed = any(ph(p) == need and _status(p)[0] == "done" for p in pk)
        started = [p for p in active if ph(p) is not None and ph(p) >= later]
        if started and not closed:
            name = t["ph_disc"] if need == 0 else t["ph_design"]
            out.append(f"{t['auto_phase']}: {name} ({', '.join(str(p.get('id')) for p in started)}).")
    return out

def build_tree(s, t, cur):
    pk = [as_dict(x) for x in as_list(s.get("pacchetti"))]
    if not pk: return ""
    sids, used = {}, set()
    for p in pk:
        b = _slug(p.get("id")); sid = b; k = 2
        while sid.lower() in used: sid = f"{b}-{k}"; k += 1
        used.add(sid.lower()); sids[id(p)] = sid
    waves = []
    for p in pk:
        w = str(p.get("wave") or "—")
        if w not in waves: waves.append(w)
    rowh, top = 62, 30
    n = len(pk); H = max(140, top * 2 + n * rowh)
    xr, xw, xp = 95, 300, 600
    ys = {}
    i = 0
    for w in waves:
        for p in pk:
            if str(p.get("wave") or "—") == w:
                ys[id(p)] = top + i * rowh + rowh / 2; i += 1
    wy = {w: sum(ys[id(p)] for p in pk if str(p.get("wave") or "—") == w) / max(1, sum(1 for p in pk if str(p.get("wave") or "—") == w)) for w in waves}
    ry = H / 2
    g = [f'<svg class="tree" viewBox="0 0 1000 {H:.0f}" role="img" aria-label="{e(t["tree"])}">']
    for w in waves:
        g.append(f'<path class="br" d="M{xr+85} {ry:.0f} C{xr+130} {ry:.0f} {xw-110} {wy[w]:.0f} {xw-62} {wy[w]:.0f}"/>')
    for p in pk:
        w = str(p.get("wave") or "—"); y = ys[id(p)]
        g.append(f'<path class="br" d="M{xw+62} {wy[w]:.0f} C{xw+150} {wy[w]:.0f} {xp-130} {y:.0f} {xp-20} {y:.0f}"/>')
        est = p.get("stima_costo")
        lab = (f"{t['est']}: " + (money(est, cur) if est not in (None, "") else "?"))
        g.append(f'<text class="cost" x="{xp - 26}" y="{y - 6:.0f}" text-anchor="end">{e(lab)}</text>')
    g.append(f'<rect class="nroot" x="{xr-85}" y="{ry-20:.0f}" width="170" height="40" rx="8"/><text class="tl" x="{xr}" y="{ry+5:.0f}" text-anchor="middle">{e(_short(s.get("progetto"), 20))}</text>')
    for w in waves:
        g.append(f'<rect class="nwave" x="{xw-62}" y="{wy[w]-17:.0f}" width="124" height="34" rx="17"/><text class="tl" x="{xw}" y="{wy[w]+5:.0f}" text-anchor="middle">{e(_short(w, 15))}</text>')
    for p in pk:
        y = ys[id(p)]; st, pc = _status(p); sid = sids[id(p)]
        node = ""
        if st == "done":
            node = f'<circle class="n-done" cx="{xp}" cy="{y:.0f}" r="17"/><path class="tick" d="M{xp-7} {y:.0f} l5 5 l10 -11"/>'
        elif st == "prog":
            import math
            frac = (pc or 0) / 100.0; r = 17; ang = 2 * math.pi * frac
            x2 = xp + r * math.sin(ang); y2 = y - r * math.cos(ang); large = 1 if frac > 0.5 else 0
            arc = (f'<circle class="n-arc" cx="{xp}" cy="{y:.0f}" r="17"/>' if frac >= 0.999 else
                   (f'<path class="n-arc" d="M{xp} {y-r:.1f} A{r} {r} 0 {large} 1 {x2:.1f} {y2:.1f}"/>' if frac > 0 else ""))
            node = (f'<circle class="n-prog" cx="{xp}" cy="{y:.0f}" r="17"/>{arc}'
                    f'<text class="pct" x="{xp}" y="{y+4:.0f}" text-anchor="middle">{e(_prog_label(p, pc))}</text>')
        else:
            node = f'<circle class="n-todo" cx="{xp}" cy="{y:.0f}" r="17"/>'
        title = str(p.get("titolo") or "")
        g.append(f'<a href="#{sid}" class="nd" data-wp="{sid}">{node}'
                 f'<text class="wid" x="{xp+28}" y="{y-3:.0f}">{e(_short(p.get("id"), 24))}</text>'
                 f'<text class="wt" x="{xp+28}" y="{y+14:.0f}">{e(title[:52] + ("…" if len(title) > 52 else ""))}</text></a>')
    g.append("</svg>")
    cards = []
    for p in pk:
        st, pc = _status(p); sid = sids[id(p)]
        stl = {"done": t["done_s"], "prog": t["prog_s"], "todo": t["todo_s"]}[st] + ((" · " + (_prog_label(p, pc) + " " + t["checks"] if _checks(p) else t["no_den"])) if st == "prog" else "")
        dels = "".join(f"<li>{e(x)}</li>" for x in as_list(p.get("deliverable")))
        sq = "".join(f'<tr><td>{e(m.get("ruolo"))}</td><td>{e(m.get("profilo"))}</td><td>{e(m.get("modello"))}</td><td>{e(m.get("ragionamento"))}</td></tr>'
                     for m in (as_dict(x, "ruolo") for x in as_list(p.get("squad"))))
        cards.append(
            f'<details class="wpc" id="{sid}"><summary><span class="dot {st}"></span><b>{e(p.get("id"))}</b> {e(p.get("titolo"))} <span class="muted">· {e(stl)}</span></summary>'
            + (f'<p><span class="lbl">{e(t["desc"])}</span><br>{e(p.get("descrizione"))}</p>' if p.get("descrizione") else "")
            + (f'<p class="lbl">{e(t["deliverable"])}</p><ul>{dels}</ul>' if dels else "")
            + f'<p class="meta"><span class="lbl">{e(t["est"])}:</span> {e(money(p.get("stima_costo"), cur)) if p.get("stima_costo") not in (None, "") else "?"}'
            + (f' · <span class="lbl">{e(t["actual"])}:</span> {e(money(p.get("costo_effettivo"), cur)) if isinstance(p.get("costo_effettivo"), (int, float)) else e(p.get("costo_effettivo"))}' if p.get("costo_effettivo") not in (None, "") else "") + '</p>'
            + (f'<p class="lbl">{e(t["squad"])}</p><div class="tbl"><table><thead><tr><th>{e(t["role"])}</th><th>{e(t["profile"])}</th><th>{e(t["model"])}</th><th>{e(t["reasoning"])}</th></tr></thead><tbody>{sq}</tbody></table></div>' if sq else "")
            + f'<p class="meta muted">{e(t["tech"])}: {e(p.get("tecnico"))} · {e(t["acc"])}: {e(p.get("accettazione"))} · {e(t["pub"])}: {e(p.get("pubblicazione"))}' + (f' · {e(t["ev"])}: {e(p.get("evidenza"))}' if p.get("evidenza") else "") + '</p>'
            + "</details>")
    legend = (f'<p class="legend"><span><span class="dot done"></span>{e(t["legend_done"])}</span><span><span class="dot prog"></span>{e(t["legend_prog"])}</span>'
              f'<span><span class="dot todo"></span>{e(t["legend_todo"])}</span></p>')
    js = ("<script>(function(){function o(h){var d=document.getElementById(h);if(!d)return;"
          "document.querySelectorAll('details.wpc').forEach(function(x){x.classList.remove('sel')});d.open=true;d.classList.add('sel');d.scrollIntoView({block:'nearest',behavior:'smooth'});}"
          "document.querySelectorAll('a.nd').forEach(function(a){a.addEventListener('click',function(ev){ev.preventDefault();o(a.getAttribute('data-wp'));history.replaceState(null,'','#'+a.getAttribute('data-wp'));});});"
          "if(location.hash)o(location.hash.slice(1));})();</script>")
    return (f'<section class="card"><h2>{e(t["tree"])}</h2><p class="muted">{e(t["tree_hint"])}</p>{legend}'
            f'<div class="treebox">{"".join(g)}</div><div class="wplist">{"".join(cards)}</div>{js}</section>')

def build_profili(s, t):
    """Role Profile attivati: da stato.profili_attivi se presente, altrimenti ricavati dalle squad dei Work Package."""
    rp = [as_dict(x, "ruolo") for x in as_list(s.get("profili_attivi"))]
    if not rp:
        acc = {}
        for p in (as_dict(x) for x in as_list(s.get("pacchetti"))):
            for m in (as_dict(x, "ruolo") for x in as_list(p.get("squad"))):
                k = (str(m.get("ruolo")), str(m.get("profilo")), str(m.get("modello")))
                d = acc.setdefault(k, {"ruolo": m.get("ruolo"), "profilo": m.get("profilo"), "modello": m.get("modello"),
                                       "ragionamento": m.get("ragionamento"), "work_package": []})
                if p.get("id") and p.get("id") not in d["work_package"]:
                    d["work_package"].append(p.get("id"))
        rp = list(acc.values())
    if not rp:
        return f'<section class="card"><h2>{e(t["rp_title"])}</h2><p class="muted">{e(t["rp_none"])}</p></section>'
    rows = "".join(
        f'<tr><td><b>{e(m.get("ruolo"))}</b>' + (f'<br><span class="muted">{e(m.get("descrizione"))}</span>' if m.get("descrizione") else "") + '</td>'
        f'<td>{e(m.get("profilo"))}</td><td>{e(m.get("qualificazione") or "—")}</td><td>{e(m.get("modello"))}</td><td>{e(m.get("ragionamento") or "—")}</td>'
        f'<td>{e(", ".join(map(str, as_list(m.get("compiti")))) or "—")}</td><td>{e(", ".join(map(str, as_list(m.get("work_package")))) or "—")}</td>'
        f'<td>{e(m.get("esecuzioni") if m.get("esecuzioni") not in (None, "") else "—")}</td></tr>' for m in rp)
    return (f'<section class="card"><h2>{e(t["rp_title"])}</h2><p class="muted">{e(t["rp_hint"])}</p><div class="tbl"><table><thead><tr>'
            f'<th>{e(t["role"])}</th><th>{e(t["profile"])}</th><th>{e(t["rp_qual"])}</th><th>{e(t["model"])}</th><th>{e(t["reasoning"])}</th>'
            f'<th>{e(t["rp_tasks"])}</th><th>{e(t["rp_wp"])}</th><th>{e(t["rp_runs"])}</th></tr></thead><tbody>{rows}</tbody></table></div></section>')

DEFAULT_DOCS = [("mandato.md", "d_mandato", "strategico"), ("architettura.md", "d_arch", "manageriale"),
                ("piano.md", "d_piano", "manageriale"), ("decisioni.md", "d_decisioni", "manageriale"),
                ("rischi.md", "d_rischi", "manageriale"), ("executive.md", "d_exec", "manageriale"),
                ("performance.md", "d_perf", "manageriale")]
_BLOCKED = ("registro.jsonl", "stato.json")

def _safe_rel(reg, rel):
    """Percorso relativo dentro eiraman/, mai fuori, mai file operativi."""
    rel = str(rel or "").replace("\\", "/").strip()
    if not rel or rel.startswith("/") or _re.match(r"^[A-Za-z]:", rel) or "://" in rel: return None
    full = os.path.realpath(os.path.join(reg, rel))
    base = os.path.realpath(reg)
    if not full.startswith(base + os.sep): return None
    r = os.path.relpath(full, base).replace(os.sep, "/")
    rl = r.lower()
    if rl in _BLOCKED or rl.startswith(("evidenze/", "vista/")) or rl in ("evidenze", "vista"): return None
    return r

_REG = None  # cartella eiraman/ del progetto, impostata da main()

def _local(href):
    """Destinazione locale ammessa (relativa a eiraman/) oppure None."""
    from urllib.parse import unquote
    dec = html.unescape(href)
    for _ in range(10):
        nxt = unquote(dec)
        if nxt == dec: break
        dec = nxt
    else:
        return None
    if "\x00" in dec: return None
    dec = dec.split("#", 1)[0].split("?", 1)[0]
    if not dec or _re.match(r"^[a-z][a-z0-9+.-]*:", dec, _re.I) or dec.startswith(("/", "\\")): return None
    return _safe_rel(_REG, dec) if _REG else None

def _q(r):
    from urllib.parse import quote
    return quote(r, safe="/")

def _inline(x):
    x = e(x)
    tok = []
    def keep(s):
        tok.append(s); return f"\x00{len(tok) - 1}\x00"
    def img(m):
        alt, src = m.group(1), m.group(2)
        r = _local(src)
        return keep(f'<img alt="{alt}" src="../../{_q(r)}">') if r else alt
    x = _re.sub(r"!\[([^\]]*)\]\(([^)\s]+)\)", img, x)
    def lnk(m):
        txt, href = m.group(1), m.group(2)
        if "\x00" in href: return txt
        if _re.match(r"^https?://", html.unescape(href), _re.I): return keep(f'<a href="{href}" rel="noopener">') + txt + keep("</a>")
        r = _local(href)
        if not r: return txt
        dest = _DOCMAP.get(r) if r.lower().endswith(".md") else None
        if r.lower().endswith(".md") and not dest: return txt
        return keep(f'<a href="{e(dest) if dest else "../../" + _q(r)}">') + txt + keep("</a>")
    x = _re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", lnk, x)
    x = _re.sub(r"`([^`]+)`", r"<code>\1</code>", x)
    x = _re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", x)
    x = _re.sub(r"(?<![\w*])\*([^*\n]+)\*(?![\w*])", r"<i>\1</i>", x)
    return _re.sub(r"\x00(\d+)\x00", lambda m: tok[int(m.group(1))], x)

_DOCMAP = {}  # percorso relativo .md -> nome della pagina generata

def _doc_page(rel):
    return _re.sub(r"[^A-Za-z0-9_-]+", "-", rel[:-3] if rel.endswith(".md") else rel).strip("-") + ".html"

def md_to_html(src):
    out, para, lst, tbl, code = [], [], None, [], None
    def flush():
        nonlocal para, lst, tbl
        if para: out.append("<p>" + _inline(" ".join(para)) + "</p>"); para = []
        if lst: out.append(f"<{lst[0]}>" + "".join(f'<li class="i{d}">{_inline(i)}</li>' for d, i in lst[1]) + f"</{lst[0]}>"); lst = None
        if tbl:
            rows = [[c.strip() for c in r.strip().strip("|").split("|")] for r in tbl if not _re.match(r"^\s*\|?[\s:|-]+\|?\s*$", r)]
            if rows:
                h = "".join(f"<th>{_inline(c)}</th>" for c in rows[0])
                b = "".join("<tr>" + "".join(f"<td>{_inline(c)}</td>" for c in r) + "</tr>" for r in rows[1:])
                out.append(f'<div class="tbl"><table><thead><tr>{h}</tr></thead><tbody>{b}</tbody></table></div>')
            tbl = []
    for line in src.splitlines():
        if code is not None:
            if line.strip().startswith("```"): out.append("<pre>" + e("\n".join(code)) + "</pre>"); code = None
            else: code.append(line)
            continue
        if line.strip().startswith("```"): flush(); code = []; continue
        m = _re.match(r"^(#{1,4})\s+(.*)$", line)
        if m: flush(); n = min(4, len(m.group(1)) + 1); out.append(f"<h{n}>{_inline(m.group(2))}</h{n}>"); continue
        if line.strip().startswith("|"): 
            if para or lst: flush()
            tbl.append(line); continue
        elif tbl: flush()
        m = _re.match(r"^(\s*)([-*]|\d+[.)])\s+(.*)$", line)
        if m:
            kind = "ol" if m.group(2)[0].isdigit() else "ul"
            if para: flush()
            if lst is None: lst = (kind, [])
            lst[1].append((min(3, len(m.group(1)) // 2), m.group(3))); continue
        if not line.strip(): flush(); continue
        if lst and line.startswith("  "): d, i = lst[1][-1]; lst[1][-1] = (d, i + " " + line.strip()); continue
        if lst: flush()
        para.append(line.strip())
    if code is not None: out.append("<pre>" + e("\n".join(code)) + "</pre>")
    flush()
    return "".join(out)

def collect_docs(s, reg, t):
    items = []
    declared = as_list(s.get("documenti"))
    if declared:
        for d in declared:
            d = as_dict(d, "percorso")
            items.append((d.get("percorso"), str(d.get("titolo") or d.get("percorso") or ""), str(d.get("livello") or "manageriale").lower(), d.get("nota")))
    else:
        for rel, key, lvl in DEFAULT_DOCS: items.append((rel, t[key], lvl, None))
        cdir = os.path.join(reg, "ciclo")
        if os.path.isdir(cdir):
            for f in sorted(os.listdir(cdir), reverse=True):
                if f.endswith(".md"): items.append((f"ciclo/{f}", f'{t["d_ciclo"]} · {f[:-3]}', "manageriale", None))
    res = []
    for rel, title, lvl, nota in items:
        r = _safe_rel(reg, rel)
        ok = bool(r) and os.path.isfile(os.path.join(reg, r))
        res.append(dict(refused=not r, rel=r or str(rel or ""), title=title, lvl="strategico" if lvl.startswith(("strateg",)) else "manageriale",
                        nota=nota, ok=ok, date=(date.fromtimestamp(os.path.getmtime(os.path.join(reg, r))).isoformat() if ok else None)))
    return res

def main():
    root = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else ".")
    reg = os.path.join(root, "eiraman")
    global _REG
    _REG = reg
    src = os.path.join(reg, "stato.json")
    if not os.path.exists(src):
        sys.exit(f"Manca {src}: il Coordinatore AI deve crearlo (vedi STATO.md).")
    try:
        s = json.load(open(src, encoding="utf-8"))
    except Exception as ex:
        sys.exit(f"{src} non è un JSON valido ({ex.__class__.__name__}): correggilo secondo STATO.md.")
    if not isinstance(s, dict):
        sys.exit(f"{src} deve contenere un oggetto JSON (vedi STATO.md).")
    lang = s.get("lingua") if isinstance(s.get("lingua"), str) and s.get("lingua") in L else "it"
    t = L[lang]

    runs = None
    rj = os.path.join(reg, "registro.jsonl")
    if os.path.exists(rj):
        runs = 0
        for line in open(rj, encoding="utf-8", errors="replace"):
            try:
                if json.loads(line).get("tipo") == "run":
                    runs += 1
            except Exception:
                pass

    b = s.get("budget") if isinstance(s.get("budget"), dict) else {}
    cur = b.get("valuta", "EUR")
    cap = b.get("tetto"); spent = b.get("speso")
    pct = None; bar_state = "unknown"
    try:
        fs = float(spent); fc = float(cap)
        if fc <= 0:
            pct, bar_state = (1.0, "stop") if fs > 0 else (0.0, "ok")
        else:
            pct = max(0.0, min(1.2, fs / fc))
            bar_state = "ok" if pct < 0.8 else ("warn" if pct < 1 else "stop")
    except Exception:
        pass

    bad = [x for x in as_list(s.get("cattive_notizie")) if x not in (None, "")]

    dos_open, dos_done = [], []
    auto = phase_alerts(s, t)
    for d in as_list(s.get("decisioni")):
        d = as_dict(d)
        st = str(d.get("stato") or "aperto").strip().lower()
        if st in ("deciso", "decided", "chiuso", "closed"):
            dos_done.append(d); continue
        dos_open.append(d)
        dl = days_left(d.get("scadenza"))
        if dl is not None and dl < 0 or st in ("scaduto", "overdue"):
            auto.append(f'{t["auto_late"]}: {d.get("id","")} {d.get("titolo","")}')
        if not d.get("scadenza") or not d.get("se_non_rispondi"):
            auto.append(f'{t["auto_missing"]}: {d.get("id","")} {d.get("titolo","")}')
    if bar_state == "warn": auto.append(t["auto_80"])
    if bar_state == "stop": auto.append(t["auto_100"])
    items = [f"<li>{e(x)}</li>" for x in bad] + [f'<li class="auto">{e(x)}</li>' for x in auto]
    bad_html = "".join(items) or f'<li class="muted">{e(t["none_bad"])}</li>'
    def do_card(d):
        dl = days_left(d.get("scadenza"))
        when = e(d.get("scadenza", "")) or f'<span class="late">{e(t["missing"])}</span>'
        if dl is not None:
            when += f' · <span class="{"late" if dl < 0 else ("soon" if dl <= 1 else "")}">' + (
                e(t["expired"]) if dl < 0 else (e(t["today"]) if dl == 0 else f"{dl} {e(t['days'])}")) + "</span>"
        opts = "".join(f'<li><b>{e(o.get("nome"))}</b> — {e(o.get("effetto"))}</li>' for o in (as_dict(x, "nome") for x in as_list(d.get("opzioni"))))
        return (f'<article class="do"><header><span class="id">{e(d.get("id"))}</span><h3>{e(d.get("titolo"))}</h3></header>'
                f'<p class="q">{e(d.get("domanda"))}</p>'
                + (f'<p class="lbl">{e(t["options"])}</p><ul class="opts">{opts}</ul>' if opts else "")
                + (f'<p><span class="lbl">{e(t["rec"])}:</span> {e(d.get("raccomandazione"))}</p>' if d.get("raccomandazione") else "")
                + f'<p class="meta"><span class="lbl">{e(t["deadline"])}:</span> {when}</p>'
                + f'<p class="meta"><span class="lbl">{e(t["ifnot"])}:</span> ' + (e(d.get("se_non_rispondi")) or f'<span class="late">{e(t["missing"])}</span>') + '</p>'
                + "</article>")
    dos_html = "".join(do_card(d) for d in dos_open) or f'<p class="muted">{e(t["none_do"])}</p>'
    done_html = "".join(f'<li><b>{e(d.get("id"))}</b> {e(d.get("titolo"))} — {e(d.get("esito"))}</li>' for d in dos_done)

    rows = "".join(
        f'<tr><td><b>{e(p.get("id"))}</b><br><span class="muted">{e(p.get("titolo"))}</span></td><td>{e(p.get("wave"))}</td>'
        f'<td>{e(p.get("tecnico"))}</td><td>{e(p.get("accettazione"))}</td><td>{e(p.get("pubblicazione"))}</td>'
        f'<td class="ev">{e(p.get("evidenza"))}</td></tr>' for p in (as_dict(x) for x in as_list(s.get("pacchetti"))))

    cyc = s.get("ciclo") if isinstance(s.get("ciclo"), dict) else {}
    ndo = s.get("escalation_ciclo"); ref = s.get("indicatore_do", 3)
    risks = "".join(f"<li>{e(x)}</li>" for x in as_list(s.get("rischi")))
    deliv = "".join(f"<li>{e(x)}</li>" for x in as_list(s.get("consegne")))

    page = f"""<!doctype html><html lang="{lang}"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(t['title'])} · {e(s.get('progetto'))}</title>
<style>
:root{{--bg:#f5f7fa;--paper:#fff;--ink:#18202b;--muted:#566273;--rule:#dde3ea;--accent:#2f5f98;--warn:#9a6a12;--stop:#9b2c2c;--ok:#3e6470;color-scheme:light}}
@media (prefers-color-scheme:dark){{:root{{--bg:#0f141b;--paper:#151c25;--ink:#e6ebf1;--muted:#9aa6b5;--rule:#253040;--accent:#8fb4e6;--warn:#e0b768;--stop:#e9a0a0;--ok:#9fc0c9;color-scheme:dark}}}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--bg);color:var(--ink);font:15px/1.5 -apple-system,"Barlow","Helvetica Neue",Arial,sans-serif}}
.wrap{{max-width:1080px;margin:0 auto;padding:24px 16px 48px;display:grid;gap:20px}}
h1{{margin:0;font-size:26px}}h2{{margin:0 0 10px;font-size:18px}}h3{{margin:0;font-size:16px}}
.top{{display:flex;flex-wrap:wrap;gap:8px 18px;color:var(--muted);font-size:13px}}.top b{{color:var(--ink)}}
.card{{background:var(--paper);border:1px solid var(--rule);border-radius:10px;padding:16px 18px;min-width:0}}
.grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:20px}}
.bad{{border-left:4px solid var(--stop)}}.bad ul{{margin:0;padding-left:18px}}
.muted{{color:var(--muted)}}.lbl{{color:var(--muted);font-size:12px;text-transform:uppercase;letter-spacing:.05em}}
.do{{border:1px solid var(--rule);border-left:4px solid var(--accent);border-radius:8px;padding:12px 14px;margin-bottom:12px}}
.do header{{display:flex;gap:10px;align-items:baseline}}.do .id{{font:600 12px ui-monospace,Menlo,monospace;color:var(--accent)}}
.do .q{{font-weight:600;margin:8px 0}}.opts{{margin:4px 0 8px;padding-left:18px}}.meta{{margin:4px 0;font-size:14px}}
.late{{color:var(--stop);font-weight:600}}.soon{{color:var(--warn);font-weight:600}}
.bar{{height:14px;border-radius:7px;background:var(--rule);position:relative;overflow:hidden;margin:10px 0 6px}}
.bar i{{position:absolute;inset:0 auto 0 0;background:var(--ok)}}.bar.warn i{{background:var(--warn)}}.bar.stop i{{background:var(--stop)}}
.bar.unknown{{background:repeating-linear-gradient(45deg,var(--rule) 0 6px,transparent 6px 12px)}}.auto{{font-style:italic}}
.bar s{{position:absolute;top:0;bottom:0;width:2px;background:var(--ink);opacity:.5}}
table{{width:100%;border-collapse:collapse;font-size:14px}}th,td{{text-align:left;padding:8px 6px;border-bottom:1px solid var(--rule);vertical-align:top}}
th{{color:var(--muted);font-weight:600;font-size:12px;text-transform:uppercase;letter-spacing:.04em}}.ev{{word-break:break-word;color:var(--muted)}}
.treebox{{overflow-x:auto}}.tree{{display:block;width:100%;min-width:720px;height:auto}}
.tree .br{{fill:none;stroke:var(--rule);stroke-width:2}}.tree .cost{{font-size:12px;fill:var(--muted)}}
.tree .nroot{{fill:var(--accent);}}.tree .nroot+.tl{{fill:var(--paper)}}.tree .nwave{{fill:var(--paper);stroke:var(--accent);stroke-width:1.5}}
.tree .tl{{font-size:13px;font-weight:600;fill:var(--ink)}}.tree .wid{{font:600 12px ui-monospace,Menlo,monospace;fill:var(--accent)}}.tree .wt{{font-size:13px;fill:var(--ink)}}
.tree .n-done{{fill:var(--ok);stroke:var(--ok)}}.tree .tick{{fill:none;stroke:var(--paper);stroke-width:3;stroke-linecap:round;stroke-linejoin:round}}
.tree .n-prog{{fill:var(--paper);stroke:var(--rule);stroke-width:4}}.tree .n-arc{{fill:none;stroke:var(--accent);stroke-width:4}}
.tree .pct{{font-size:10px;font-weight:700;fill:var(--ink)}}.tree .n-todo{{fill:var(--paper);stroke:var(--muted);stroke-width:2;stroke-dasharray:4 3}}
.tree a.nd{{cursor:pointer}}.tree a.nd:hover circle,.tree a.nd:focus circle{{stroke:var(--accent);stroke-width:4}}
.legend{{display:flex;flex-wrap:wrap;gap:6px 16px;font-size:13px;color:var(--muted)}}.legend span{{display:inline-flex;align-items:center;gap:6px}}
.dot{{display:inline-block;width:12px;height:12px;border-radius:50%;vertical-align:middle;margin-right:4px}}.dot.done{{background:var(--ok)}}.dot.prog{{background:var(--paper);border:3px solid var(--accent)}}.dot.todo{{border:2px dashed var(--muted)}}
.wplist{{display:grid;gap:8px;margin-top:12px}}.wpc{{border:1px solid var(--rule);border-radius:8px;padding:8px 12px}}.wpc summary{{cursor:pointer}}
.wpc.sel{{border-color:var(--accent);box-shadow:0 0 0 2px var(--accent) inset}}
.nav{{display:flex;gap:18px;font-size:14px}}.nav a{{color:var(--accent)}}.doc h2,.doc h3,.doc h4{{margin:18px 0 8px}}.doc li.i1{{margin-left:20px}}.doc li.i2{{margin-left:40px}}.doc li.i3{{margin-left:60px}}.doc img{{max-width:100%;height:auto;background:#fff;border-radius:6px}}.doc pre{{overflow-x:auto;background:var(--bg);padding:10px;border-radius:6px}}.doclist li{{margin:6px 0}}.doclist .na{{color:var(--muted)}}
.tbl{{overflow-x:auto}}footer{{color:var(--muted);font-size:13px}}
</style></head><body><div class="wrap">
<nav class="nav"><b>{e(t['nav_view'])}</b><a href="documenti.html">{e(t['nav_docs'])}</a></nav>
<header><h1>{e(t['title'])} · {e(s.get('progetto'))}</h1>
<div class="top"><span>{e(t['phase'])}: <b>{e(s.get('fase'))}</b></span><span>{e(t['cls'])}: <b>{e(s.get('classe'))}</b></span>
<span>{e(t['lvl'])}: <b>{e(s.get('livello'))}</b></span><span>{e(t['cycle'])}: <b>{e(cyc.get('numero'))}</b> ({e(cyc.get('inizio'))} → {e(t['review'])} {e(cyc.get('revisione'))})</span>
<span>{e(t['updated'])}: <b>{e(s.get('aggiornato'))}</b></span></div>
{f'<p class="muted">{e(t["vision"])}: {e(s.get("visione"))}</p>' if s.get("visione") else ""}</header>
<section class="card bad"><h2>{e(t['bad'])}</h2><ul>{bad_html}</ul></section>
<div class="grid">
<section class="card"><h2>{e(t['dos'])}</h2>{dos_html}
{f'<p class="lbl">{e(t["decided"])}</p><ul>{done_html}</ul>' if done_html else ""}
{f'<p class="muted">{e(t["do_count"])}: {e(ndo)} ({e(t["ref"])} {e(ref)})</p>' if ndo is not None else ""}</section>
<section class="card"><h2>{e(t['budget'])}</h2>
<p><b>{e(money(spent, cur))}</b> {e(t['spent'])} · {e(t['cap'])} {e(money(cap, cur))}</p>
<div class="bar {bar_state}" role="img" aria-label="{e(t['budget'])}"><i style="width:{0 if pct is None else min(pct,1)*100:.0f}%"></i><s style="left:80%"></s></div>
{f'<p class="muted">{e(t["unknown_spend"])}</p>' if bar_state=="unknown" else ""}{f'<p class="soon">{e(t["alert80"])}</p>' if bar_state=="warn" else ""}{f'<p class="late">{e(t["block100"])}</p>' if bar_state=="stop" else ""}
{f'<p class="muted">{e(b.get("sconosciuto"))} {e(t["unknown"])}. {e(b.get("nota",""))}</p>' if b.get("sconosciuto") else ""}
<p class="muted">{e(t['runs']) + ': ' + str(runs) if runs is not None else e(t['no_reg'])}</p>
<p class="muted">{e(t['gov_share'])}: {e(_share(cyc.get('quota_governo'), 'governo', 'totale', t, cur))} · {e(t['off_cat'])}: {e(_share(cyc.get('fuori_catalogo'), 'task', 'totale', t))}</p>
{f'<h2>{e(t["risks"])}</h2><ul>{risks}</ul>' if risks else ""}</section>
</div>
{build_profili(s, t)}
{build_tree(s, t, cur)}
<section class="card"><h2>{e(t['pk'])}</h2><div class="tbl"><table><thead><tr><th>ID</th><th>Wave</th><th>{e(t['tech'])}</th><th>{e(t['acc'])}</th><th>{e(t['pub'])}</th><th>{e(t['ev'])}</th></tr></thead><tbody>{rows}</tbody></table></div></section>
<div class="grid">
{f'<section class="card"><h2>{e(t["deliv"])}</h2><ul>{deliv}</ul></section>' if deliv else ""}
{f'<section class="card"><h2>{e(t["next"])}</h2><p>{e(s.get("prossimo_ciclo"))}</p></section>' if s.get("prossimo_ciclo") else ""}
</div>
<footer>{e(t['foot'])}</footer>
</div></body></html>"""
    out_dir = os.path.join(reg, "vista"); os.makedirs(out_dir, exist_ok=True)
    out = os.path.join(out_dir, "index.html")
    open(out, "w", encoding="utf-8").write(page)
    write_docs(s, reg, t, out_dir, page)
    print(out)

def write_docs(s, reg, t, out_dir, page):
    head = page.split("<body>", 1)[0].replace(f"<title>", "<title>", 1)
    _tt = f"<title>{e(t['docs_title'])} · {e(s.get('progetto'))}</title>"
    head = _re.sub(r"<title>.*?</title>", lambda m: _tt, head, flags=_re.S)
    ddir = os.path.join(out_dir, "doc"); os.makedirs(ddir, exist_ok=True)
    for f in os.listdir(ddir):
        if f.endswith(".html"): os.remove(os.path.join(ddir, f))
    docs = collect_docs(s, reg, t)
    _DOCMAP.clear(); used = set()
    for d in docs:
        if d["ok"]:
            base = _doc_page(d["rel"])[:-5]; name = base + ".html"; k = 2
            while name.lower() in used: name = f"{base}-{k}.html"; k += 1
            used.add(name.lower()); _DOCMAP[d["rel"]] = name
    def li(d):
        if not d["ok"]:
            return f'<li class="na">{e(d["title"])} · {e(t["refused"] if d.get("refused") else t["absent"])}</li>'
        name = _DOCMAP[d["rel"]]
        body = md_to_html(open(os.path.join(reg, d["rel"]), encoding="utf-8", errors="replace").read())
        open(os.path.join(ddir, name), "w", encoding="utf-8").write(
            head.replace(f"<title>{e(t['docs_title'])}", f"<title>{e(d['title'])}") + "<body><div class=\"wrap\">"
            f'<nav class="nav"><a href="../index.html">{e(t["nav_view"])}</a><a href="../documenti.html">{e(t["back"])}</a></nav>'
            f'<article class="card doc"><p class="lbl">{e(d["title"])} · {e(d["date"])}</p>{body}</article></div></body></html>')
        return (f'<li><a href="doc/{e(name)}">{e(d["title"])}</a> <span class="muted">· {e(d["date"])}</span>'
                + (f'<br><span class="muted">{e(d["nota"])}</span>' if d.get("nota") else "") + "</li>")
    sect = ""
    for lvl, lab in (("strategico", t["strategic"]), ("manageriale", t["managerial"])):
        its = "".join(li(d) for d in docs if d["lvl"] == lvl)
        if its: sect += f'<section class="card"><h2>{e(lab)}</h2><ul class="doclist">{its}</ul></section>'
    open(os.path.join(out_dir, "documenti.html"), "w", encoding="utf-8").write(
        head + '<body><div class="wrap">'
        f'<nav class="nav"><a href="index.html">{e(t["nav_view"])}</a><b>{e(t["nav_docs"])}</b></nav>'
        f'<header><h1>{e(t["docs_title"])} · {e(s.get("progetto"))}</h1><p class="muted">{e(t["docs_hint"])}</p></header>'
        f'{sect}<footer>{e(t["foot"])}</footer></div></body></html>')

if __name__ == "__main__":
    main()
