# AI-Driven Development

Source: `/home/ff/Documents/Projects/the-last-light/g.Presentations/curated/AI-Driven Development.pptx`
Slides: 58

## Slide 1
AI-Driven Development
Van vibe coding naar controleerbare AI-coding workflows

## Slide 2
Vibe coding is snel. Maar wat bewijst het?
Code genereren is makkelijk
Verifiëren blijft moeilijk
Overdragen is vaak nog moeilijker

## Slide 3
Herkenbaar? De agent zegt "done", jij bent twee uur kwijt.
Deze training gaat niet over "nog betere prompts". Ze gaat over controle terugnemen.
Tests niet gedraaid
Verkeerde runtime
30 files voor één bug
Volgende sessie weet niets

## Slide 4
Moet je elke tussenstap nog lezen?
Nee, niet altijd. Maar je moet eerst proefmatig ontdekken welke taken veilig autonoom kunnen lopen.
De workflow is ontstaan door experimenteren
Kleine taken uitvoeren, proof bundles controleren
CTO-agent review vergelijken met menselijke review
Autonomie stapsgewijs verhogen
Batchgrootte verhogen als bewijs stijgt

## Slide 5
Onze case: PersonaLab
Een gecontroleerde demo-app voor AI-persona's, toestemming en bewijs
AI-persona's zijn herkenbaar en risicovol
Scope, consent en bewijs zijn cruciaal
We volgen BL-002 Consent Gate

## Slide 6
01.
Het Probleem
Waarom AI coding agents vaak ontsporen

## Slide 7
01.
Context Decay
Beslissingen verdwijnen in chat history. De agent vergeet. Nieuwe sessies starten blind.

## Slide 8
01.
Fake Progress
"Implemented" zonder werkende code. Screenshot zonder runtime identity.

## Slide 9
01.
Het echte probleem is ontbrekende projectwaarheid
Chat is vluchtig
Repo-state is onduidelijk
Runtime kan afwijken
"Klaar" = niets zonder bewijs

## Slide 10
01.
Van losse prompts naar een workflow
1
Losse prompt
2
Betere prompt
3
State files
4
Tools
5
Proof bundle
6
CTO review
7
Team workflow

## Slide 11
02.
StateDD als Project-OS
De repo als bron van waarheid

## Slide 12
02.
De repo als bron van waarheid
Chat is voor communicatie. De repo is voor waarheid.
Persistent
Versioned
Gedeelde truth
Machine-readable

## Slide 13
02.
De StateDD Control Loop
Plan
Execute
Verify
Record
Handoff
Review
Next Action
Human/CTO kiest richting
Coding agent voert uit
Tools verifiëren
Proof bundle bewaart bewijs
CTO beoordeelt

## Slide 14
02.
De volledige StateDD-template
StateDD werkt omdat deze bestanden samen één gedeelde projectwaarheid vormen.
AGENTS.md
STATUS.md
PROJECT_STATE.yaml
PROJECT_DNA.yaml
NEXT_ACTIONS.md
BACKLOG.md
EVIDENCE_LOG.md

## Slide 15
02.
Rol per file

## Slide 16
02.
Waarom niet zomaar files overslaan?
Eén ontbrekende state-laag wordt later vaak context decay.
Geen AGENTS.md → Elke agent verzint zijn eigen rol
Geen STATUS.md → Niemand weet wat er al gedaan is
Geen PROJECT_STATE.yaml → Technische state verdwijnt
Geen PROJECT_DNA.yaml → Stack en aannames zijn onzichtbaar
Geen NEXT_ACTIONS.md → Sessies starten zonder richting
Geen BACKLOG.md → Scope en voortgang zijn vaag
Geen EVIDENCE_LOG.md → Bewijs is verspreid en verloren

## Slide 17
02.
Begin klein, maar gebruik de volledige template
Je begint klein in gedrag: één backlog slice, één proof bundle, één handoff. Niet klein in waarheid: geen ontbrekende state-laag.
Start vanuit volledige template
Alle files blijven aanwezig
De template voorkomt dat elke agent zijn eigen proces verzint

## Slide 18
03.
Van CTO-beslissing naar Werkcontract
De CTO vertaalt doel naar controleerbare opdracht

## Slide 19
03.
De mens is supervisor, niet bottleneck
Het doel is niet dat de mens elke stap controleert. Het doel is dat de mens weet wanneer controle nodig is.
De mens bepaalt doelen, risico's en grenzen
De CTO-agent vertaalt dit naar werkcontracten
De coding agent voert uit
De CTO-agent reviewt proof bundles
De mens leest steekproeven, escalaties en eindresultaten
Het systeem leert waar autonomie veilig is

## Slide 20
03.
De CTO maakt het werkcontract
De coding agent krijgt geen wens. Hij krijgt een controleerbaar werkcontract.
Productdoel → scope
Risico's → out-of-scope
"Klaar" → acceptance criteria
Tools → bewijs
Geen open einde

## Slide 21
03.
Slechte prompt vs Werkcontract BL-002
Slecht
"Bouw een AI-kloon app"
• Geen scope
• Geen acceptance criteria
• Geen bewijsverplichting
• Open einde
• Agent verzint zelf wat "klaar" betekent
Werkcontract BL-002
Consent Gate implementeren
• Duidelijke scope
• Expliciete out-of-scope
• 4 acceptance criteria
• Proof bundle verplicht
• CTO review gate

## Slide 22
03.
Scope, Out-of-Scope & Acceptance Criteria
Scope
• Consent selector UI
• Blocking ontbreekt-toestemming
• Audit log
Out-of-Scope
• Voice cloning
• Face synthesis
• Data scraping
• Persistent memory
Acceptance Criteria
• Block unauthorized
• Warning visible
• Tests pass
• Browser proof

## Slide 23
03.
Closure Gates
Elke sessie eindigt pas als alle gates expliciet beantwoord zijn.
Geen ongerelateerde changes
Geen "klaar" zonder bewijs
Tests geslaagd
Runtime identity bewezen
Worktree clean

## Slide 24
03.
Human-in-the-loop, human-on-the-loop, human-out-of-the-loop
De vraag is niet: "moet ik alles zelf reviewen?" De vraag is: "welke taken kan ik veilig delegeren?"
Human-in-the-loop
Mens controleert elke belangrijke stap vóór voortgang
Human-on-the-loop
Agents werken zelfstandig binnen grenzen. Mens monitort, doet steekproeven, grijpt in bij risico's
Human-out-of-the-loop
Voor repetitieve, goed afgebakende, goed geteste taken kan de agentketen meerdere slices autonoom afwerken

## Slide 25
04.
Subagents & MCP
Waarom één agent niet alles zelf mag doen

## Slide 26
04.
Het probleem met de alles-in-één agent
Een agent die zelf bouwt, test, bewijst en zichzelf goedkeurt = te veel macht.
Alsof een aannemer zijn eigen bouwvergunning, inspectie en opleveringsrapport schrijft.

## Slide 27
04.
Subagents: geen zelfkeuring
Geen agent beoordeelt zijn eigen werk.
1. Coding Agent
Bouwt en implementeert
2. Test Agent
Verifieert en valideert
3. Evidence Agent
Verzamelt bewijs
4. Documentation Agent
Houdt state bij
5. Review / CTO Agent
Beoordeelt en beslist

## Slide 28
04.
MCP: tools in plaats van gokken
MCP verbindt agents met echte output.
Agent Brain
Krijgt een werkcontract en denkt na
→ MCP Layer
Standaard protocol naar tools
→ Gereedschapsarmen
Git, terminal, browser, database
→ Echte Output
Commits, screenshots, logs, testresultaten

## Slide 29
04.
9 MCP Types
Git
Commits, branches, diffs
Terminal
Shell commands, scripts
Browser
Web, screenshots, DOM
Database
Queries, migraties, schema
Test Runner
Unit, integratie, e2e
File System
Lezen, schrijven, zoeken
API / HTTP
Endpoints, webhooks, REST
Documentation
State, logs, overdracht
Build / Deploy
CI/CD, packaging, release

## Slide 30
04.
Niet elke agent krijgt elk gereedschap
MCP zonder permissies is gewoon een snellere manier om chaos te maken.

## Slide 31
05.
Proof Bundles & Autonomie
"No proof, no closure"

## Slide 32
05.
Chat claim vs Proof Bundle
De chat is vluchtig. De proof bundle is persistent, genummerd, reviewbaar.
Chat claim
Vluchtig
Niet genummerd
Niet reproduceerbaar
Niet reviewbaar
Geen bewijs van runtime
Proof bundle
Persistent
Genummerd
Reproduceerbaar
Reviewbaar
Runtime bewezen

## Slide 33
05.
De proof bundle is de overdracht
Elke sessie krijgt een nieuwe genummerde evidence folder.
PersonaLab / BL-002
evidence/
BL-002-001/
test-results.json
browser-screenshot.png
console-log.txt
git-diff.patch
proof-manifest.yaml
BL-002-002/
test-results.json
browser-screenshot.png
console-log.txt
git-diff.patch
proof-manifest.yaml
BL-002-003/
...
Elke slice = eigen folder — Nummering volgt de backlog slice.
Test-resultaten — JSON met pass/fail per test.
Browser proof — Screenshot van werkende UI.
Console log — Runtime errors en warnings.
Git diff — Wat is er precies gewijzigd?
Proof manifest — Samenvatting voor CTO review.

## Slide 34
05.
"No proof, no closure"
Een claim zonder bewijs is geen voortgang. Het is een risico.
Geen tests? Niet klaar.
Geen browser proof? Niet bewezen.
Dirty worktree? Niet overdraagbaar.

## Slide 35
05.
CTO Review: drie mogelijke uitkomsten
ACCEPTED
Scope compleet
Tests pass
Proof bundle OK
State geupdate
→ Door naar next action
CONDITIONAL
Gedeeltelijk compleet
Minor issues gevonden
Proof onvolledig
→ Menselijke review nodig
REJECTED
Scope niet gehaald
Tests falen
Proof ontbreekt
State niet geupdate
→ Terug naar coding agent
Het doel is niet dat alles altijd perfect is.
Het doel is dat de status eerlijk is.

## Slide 36
05.
CTO-review hoeft niet altijd menselijk te zijn
De CTO-agent is de dagelijkse reviewer. De mens bewaakt het systeem.
De CTO-agent controleert scope, proof, tests en state
De mens controleert steekproeven en uitzonderingen
Bij lage-risico ACCEPTED-runs kan de workflow automatisch door
Bij CONDITIONAL of REJECTED stopt de keten of escaleert naar mens

## Slide 37
05.
Agentketen met escalatie

## Slide 38
05.
Demo: PersonaLab BL-002 in 7 stappen
1
CTO kiest backlog slice
2
CTO schrijft werkcontract
3
Coding agent bouwt + test
4
Browser proof (screenshot)
5
Proof bundle aangemaakt
6
CTO-agent reviewt resultaat
7
State update + next action
BL-002 Consent Gate
Deze 7 stappen worden gevolgd voor elke backlog slice in de PersonaLab demo.
Elke stap produceert bewijs dat de volgende stap kan controleren.
Geen stap slaat over naar de volgende zonder een duidelijke handoff.
De CTO-agent reviewt het eindresultaat en bepaalt of de keten door mag.

## Slide 39
05.
Wanneer mag de agentketen doorwerken?
Autonomie werkt het best bij kleine, bewijsbare, herhaalbare taken.
Kleine backlog slices
Duidelijke acceptance criteria
Bestaande testdekking
Geen productie- of security-impact
Geen nieuwe architectuur
Volledige proof bundle
Clean worktree
CTO-agent review = ACCEPTED
Volgende NEXT_ACTION is logisch en laag risico

## Slide 40
06.
Workshop, Autonomie & Maturity
Van niveau 0 naar niveau 5

## Slide 41
06.
De autonomie-ladder
Autonomie is iets dat je verdient met bewijs.
Level 0 — Mens leest elke stap
Level 1 — Mens leest elke handoff
Level 2 — CTO-agent reviewt, mens doet steekproeven
Level 3 — Agents werken 2–3 slices autonoom af
Level 4 — Agents werken een batch af met escalation gates
Level 5 — Mens stuurt op doelen, risico's en eindresultaat

## Slide 42
06.
Wanneer lees je als mens wél de handoff?
Je leest niet alles. Je leest wat risico draagt.
Productie-impact
Security / auth / permissions
Persoonsgegevens of consent
Database migraties
Externe API's of echte netwerkacties
Nieuwe architectuurbeslissingen
Dirty worktree
Ontbrekende proof bundle
Failed tests
Scope drift
CTO-agent zegt CONDITIONAL of REJECTED

## Slide 43
06.
Autonomie ontwerp je proefmatig
Deze workflow is niet ontstaan uit theorie, maar uit veel experimenteren.
Start met één slice
Vergelijk CTO-agent review met menselijke review
Noteer fouten en gemiste signalen
Voeg closure gates toe
Laat daarna 2 slices na elkaar lopen
Verhoog pas de batchgrootte als bewijs goed blijft

## Slide 44
06.
Autonomy Budget
Geef agents geen onbeperkte vrijheid. Geef ze een autonomie-budget.
Autonomy Budget — PersonaLab BL-002
Max backlog items: 3
Max changed files per slice: 8
Allowed risk: low / medium
Human review required on:
security, auth, data, architecture, failed tests
Stop conditions:
dirty worktree, missing proof, scope drift, rejected CTO review

## Slide 45
06.
Agenda: Halve dag (3.5 uur)
09:00 – 09:20 Opening & het probleem
09:20 – 10:00 StateDD als Project-OS
10:00 – 10:20 Pauze
10:20 – 11:00 CTO-beslissing naar werkcontract
11:00 – 11:30 Subagents & MCP
11:30 – 12:00 Proof bundles & autonomie
12:00 – 12:20 Autonomie-ladder & budget
12:20 – 12:30 Takeaways & vragen

## Slide 46
06.
Agenda: Hele dag (7 uur)

## Slide 47
06.
Workshop: Kalibreer je autonomiegrens
De vraag is niet: "moet ik alles zelf reviewen?" De vraag is: "welke taken kan ik veilig delegeren, en waar moet het systeem escaleren?"
1. Welke delen zou je zelf lezen?
2. Welke delen mag de CTO-agent zelfstandig beoordelen?
3. Welke signalen verplichten menselijke review?
4. Mag de agentketen na ACCEPTED automatisch door?
5. Hoeveel backlog slices zonder menselijke tussenkomst?
6. Wat is het autonomy budget?
7. Welke escalation gates voeg je toe?
Deelnemers bepalen welke taken veilig autonoom kunnen lopen.

## Slide 48
06.
Hele-dag outputs
✓ StateDD-template geïnitialiseerd
✓ Rol van alle 7 files begrepen
✓ Backlog slice geanalyseerd
✓ CTO-werkcontract beoordeeld
✓ Proof bundle gecontroleerd
✓ CTO-agent review geïnterpreteerd
✓ Autonomy budget opgesteld
✓ Escalation policy opgesteld
✓ Slices autonoom bepaald
✓ Human review triggers bepaald
✓ Next action gekozen op bewijs

## Slide 49
06.
Wat je morgen kan doen
1. Start met 1 laag-risico slice en laat CTO-agent reviewen
2. Lees de eerste proof bundles zelf
3. Vergelijk menselijke review met agent-review
4. Definieer stop conditions en escalation gates
5. Laat daarna pas 2-3 slices autonoom lopen
6. Geef agents geen onbeperkte vrijheid — geef ze een budget

## Slide 50
06.
Begin met één regel
Geen claim zonder bewijs.
Je hoeft geen perfect systeem
Niet alles tegelijk
Begin met één regel
Één team, één week, één slice

## Slide 51
06.
De toekomst is niet: betere prompts. De toekomst is: betere workflows rond agents.
StateDD is geen prompttruc
Het is een herbruikbaar project-OS voor AI-driven development
De vraag verschuift van "kan ik de agent vertrouwen?" naar "onder welke voorwaarden mag deze agentketen zelfstandig verder?"

## Slide 52
Vragen?
github.com/lennertvhoy/StateDD_Template
Open source · MIT licensed

## Slide 53
APPENDIX
Coding-Agent Prompt
PERSONA: Senior full-stack developer. STRICT RULES:
1. Read ALL 7 StateDD files BEFORE coding
2. Follow workcontract scope EXACTLY
3. Run tests BEFORE claiming done
4. Create proof bundle with screenshots + logs
5. Update STATUS.md + PROJECT_STATE.yaml
6. NO changes outside assigned files
7. STOP and escalate on scope drift
READ ORDER:
1. AGENTS.md → roles & rules
2. PROJECT_DNA.yaml → identity & stack
3. STATUS.md → current state
4. BACKLOG.md → priorities
5. NEXT_ACTIONS.md → immediate task
6. PROJECT_STATE.yaml → technical snapshot
7. EVIDENCE_LOG.md → previous proofs
EXAMPLE — BL-002 Consent Gate:
Scope: consent selector + blocking + audit log
Acceptance: tests pass, browser proof, clean worktree
Deze prompt wordt normaal opgesteld door de CTO/human of CTO-agent.

## Slide 54
APPENDIX
CTO-Review Checklist
1. Scope compliance — alleen toegewezen files gewijzigd?
2. Tests — alle tests slagen?
3. Browser proof — screenshot met runtime identity?
4. Worktree clean — geen uncommitted changes?
5. STATUS.md bijgewerkt — state reflecteert werkelijkheid?
6. PROJECT_STATE.yaml actueel — technische snapshot klopt?
7. Evidence folder genummerd — E### formaat?
8. Proof manifest compleet — alle vereiste artifacts?
9. Geen scope drift — geen ongerelateerde wijzigingen?
10. NEXT_ACTIONS.md logisch — duidelijk vervolg?
11. Risico-beoordeling — veilig om verder te gaan?
ACCEPTED → auto-continue | CONDITIONAL → human review plan | REJECTED → stop, full review
De CTO beoordeelt, niet de coding agent.

## Slide 55
APPENDIX
Proof Manifest YAML — BL-002
proof_manifest:
slice_id: "BL-002"
status: "complete"
artifacts:
- type: test_log
path: evidence/E001/tests.log
status: pass
- type: browser_proof
path: evidence/E001/browser.png
status: verified
- type: git_diff
path: evidence/E001/changes.diff
status: clean
closure_gates:
- scope_compliant
- tests_pass
- proof_complete
- worktree_clean
review_status: ACCEPTED

## Slide 56
APPENDIX
Closure Gates
1. Geen ongerelateerde changes in de slice
2. Geen "klaar" zonder bewijs
3. Alle tests geslaagd
4. Runtime identity bewezen (browser screenshot)
5. Worktree clean — geen uncommitted changes
6. STATUS.md bijgewerkt met huidige state
7. PROJECT_STATE.yaml bijgewerkt
8. NEXT_ACTIONS.md logisch en risico-beoordeeld
Elke sessie eindigt pas als alle gates expliciet beantwoord zijn.

## Slide 57
APPENDIX
Autonomy Budget Template
Max backlog items per batch: 3
Max changed files per slice: 8
Allowed risk level: low / medium
Human review REQUIRED on:
• security, auth, permissions
• persoonsgegevens / consent
• database migraties
• externe API's of netwerkacties
• architectuurwijzigingen
• failed tests
STOP conditions (escaleer direct):
• dirty worktree
• missing proof bundle
• scope drift gedetecteerd
• CTO review = REJECTED
• tests falen

## Slide 58
APPENDIX
Proof Bundle Folder — BL-002
personalab/
├── evidence/
│ └── E001_consent_gate/
│ ├── browser_proof.png
│ ├── test_log.txt
│ ├── git_diff.patch
│ └── proof_manifest.yaml
├── state/
│ ├── AGENTS.md
│ ├── STATUS.md
│ ├── PROJECT_STATE.yaml
│ ├── PROJECT_DNA.yaml
│ ├── NEXT_ACTIONS.md
│ ├── BACKLOG.md
│ └── EVIDENCE_LOG.md
└── src/
└── ...
