# StateDD v2_ Controleerbare AI-Coding Workflow

Source: `/home/ff/Documents/Projects/the-last-light/g.Presentations/curated/StateDD v2_ Controleerbare AI-Coding Workflow.pptx`
Slides: 44

## Slide 1
StateDD: Controleerbare AI-Coding Workflow
Van "het lijkt te werken" naar bewezen, genummerd, overdraagbaar, reviewbaar

## Slide 2
Vibe coding vs StateDD
Vibe Coding
Vibe coding eindigt bij:
"Het lijkt te werken"
Chat history als enige bron
Agent beoordeelt zichzelf
Geen bewijs, geen nummering
Geen overdraagbaarheid
StateDD
StateDD eindigt bij:
"Het is bewezen"
Repo als bron van waarheid
CTO agent beoordeelt werk van coding agent
Genummerde proof bundles
Volledig overdraagbaar tussen sessies

## Slide 3
Halve dag vs Hele dag
Halve Dag (3.5u)
Probleem begrijpen
StateDD principes + files
Prompt → werkcontract
Subagents + MCP intro
Proof bundles + CTO review
Demo
Mini-oefening + takeaways
Hele Dag (7u)
Alles uit halve dag
Diepgaande modules
Deelnemers bouwen zelf:
• Mini AGENTS.md
• Mini PROJECT_STATE.yaml
• 3 backlog items + 1 NEXT_ACTION
• Coding-agent prompt
• Proof bundle contract
• CTO-review prompt
Peer review
Maturity ladder
Team adoptie

## Slide 4
01.
Het Probleem
Waarom AI coding agents vaak ontsporen

## Slide 5
01.
Context Decay & Hallucinated Completion
1. Schone Start
2. Context Verlies
3. Hallucinated Completion
Hoe dit eruit ziet
Agent zegt "implemented" maar file is leeg
Agent claimt "tested" maar tests falen
Agent beschrijft features die niet bestaan
Agent vertrouwt op "geheugen" dat niet bestaat

## Slide 6
01.
Fake Progress & Over-Eager Refactoring
Fake Progress
"Klaar" = file is aangeraakt, niet getest
"Werkt" = compileert, niet gevalideerd
Screenshot van UI zonder runtime identity
Commit zonder verificatie
Over-Eager Refactoring
Agent herstructureert hele codebase voor 1 kleine feature
50 files gewijzigd voor 1 regel functionele wijziging
Geen scope grenzen → agent doet wat het "logisch" vindt
Bestaande architectuur wordt genegeerd

## Slide 7
01.
Runtime Confusion & Screenshots Zonder Bewijswaarde
Runtime Confusion
Meerdere instanties draaien, agent weet niet welke
Agent screenshot op localhost:3000, maar code draait op localhost:3001
Stale processen geven vals positieve feedback
localhost:3000
localhost:3001
Agent weet niet welke runtime echt actief is
Screenshots Zonder Bewijswaarde
Geen repo path → welke codebase?
Geen branch/commit → welke versie?
Geen endpoint → welke runtime?
Geen timestamp → wanneer?
Geen reproduceerstappen → hoe?

## Slide 8
01.
De Scherpe Scheiding

## Slide 9
01.
De Echte Vijand is Geen Domme AI
De echte vijand is niet domme AI.
De echte vijand is ontbrekende projectwaarheid.
AI is krachtig maar stateless
Het project heeft geen gedeelde bron van waarheid
Mens en agent werken uit verschillende "waarheden"
Beslissingen verdwijnen in chat, niet in repo
Er is geen scheiding tussen wie bouwt en wie beoordeelt

## Slide 10
02.
StateDD als Project-OS
De repo als bron van waarheid

## Slide 11
02.
De Repo als Bron van Waarheid
Chat als bron (fout)
• Vluchtig — verdwijnt bij nieuwe sessie
• Niet reproducerbaar
• Geen versioning
• Alleen de agent die chatte weet wat er besloten is
• Moeilijk te auditen
Repo als bron (goed)
• Persistent — leeft na elke sessie
• Versioned via git
• Iedereen (mens en agent) leest dezelfde truth
• Audit trail in git history
• Machine-readable via YAML

## Slide 12
02.
De 6 Core Files als Systeem
AGENTS.md
PROJECT_DNA.yaml
PROJECT_STATE.yaml
BACKLOG.md
NEXT_ACTIONS.md
EVIDENCE_LOG.md
STATUS.md
DNA = stabiel | STATE = actueel | BACKLOG = plannen | NEXT_ACTIONS = uitvoeren | EVIDENCE = vertrouwen

## Slide 13
02.
AGENTS.md — Het Operating Contract
# StateDD Agent Operating Contract
## Repo Mode
- bootstrap | operating
## Universal Rules
- No fake completeness
- No unverified claims
- User-facing requires verification
- Negative searches stay negative
- Active queue max 10 items
## Startup Order
1. AGENTS.md
2. STATUS.md
3. PROJECT_STATE.yaml
4. PROJECT_DNA.yaml
5. NEXT_ACTIONS.md
6. BACKLOG.md
Wat bevat AGENTS.md?
Universele regels
• No fake completeness
• No unverified claims as fact
• User-facing requires direct verification
• Negative searches stay negative
• Active queue stays short (max 10)
Startup regels
• Lees AGENTS.md eerst
• Anker op verified truth
• Definieer één coherent scope
• Vraag bij onduidelijkheid

## Slide 14
02.
Truth als Code
PROJECT_DNA.yaml
Stabiel, zelden wijzigend
project:
name: "app"
type: "web"
tech_stack:
languages: ["java"]
frameworks: ["spring"]
governance:
decision_records: []
architecture:
patterns: ["mvc"]
conventions: ["rest"]
PROJECT_STATE.yaml
Actueel, per sessie updaten
metadata:
updated_at: "2024-05-04"
version: "2.0"
workflow:
repo_mode: operating
current_state:
repository: clean
runtime_identity: ...
verification_labels:
observed: []
unknown: []
blocked: []

## Slide 15
02.
Queue Discipline
NEXT_ACTIONS.md
Korte, actieve queue
Max 10 items
Alleen open, actief werk
Verwijst naar backlog ID: [BL-001]
Owner + next action + exit criteria
Remove completed items immediately
WATCHLIST signaleert risico's
BACKLOG.md
Medium-term roadmap
Stable IDs: BL-001, BL-002...
NOW / NEXT / LATER / WATCHLIST
Per item: title, description, acceptance criteria, priority

## Slide 16
02.
Bewijs & Snapshot
EVIDENCE_LOG.md
Structured ledger of proof artifacts
Entry format: EV-YYYY-MM-DD-001
Per entry:
File path to artifact
Source / system
Action taken
Claim it proves
Store under docs/evidence/
Rule: every claim needs proof
STATUS.md
Human-readable summary
Niet machine-checkable — bewust
Bevat:
Samenvatting PROJECT_STATE.yaml
NEXT_ACTIONS.md status
Belangrijke beslissingen
Blockers / known issues
Updated per sessie
Startpunt voor menselijke review
Teamlead checkt STATUS.md in 30 sec
EVIDENCE_LOG.md maakt claims bewijsbaar. STATUS.md maakt status begrijpelijk.

## Slide 17
03.
Van Prompt naar Werkcontract
Scope, criteria, verificatie, handoff

## Slide 18
03.
Slecht vs Goed Prompting
Slecht
"Fix de bug"
"Maak een login pagina"
"Refactor de hele app"
"Het werkt niet, doe maar iets"
Geen state files gelezen
Geen verificatie, geen evidence
Goed / StateDD-style
Lees AGENTS.md, STATUS.md, PROJECT_STATE.yaml, NEXT_ACTIONS.md
Implementeer [BL-003]: email validatie. Scope: UserService.java + test.
Acceptance: input valideert, tests passen, screenshot van error state
Verifieer: run tests, update EVIDENCE_LOG.md
Eindig met handoff: wat veranderd, wat bewezen, next action

## Slide 19
03.
Scope, Out-of-Scope & Acceptance Criteria
Scope (wat WEL)
Één backlog item
Concrete files/modules
Duidelijke functionaliteit
Voorbeeld: "Validatie logica in UserService.validateEmail()"
Out-of-Scope
UI wijzigingen (tenzij expliciet)
Database migraties
Refactoring van andere modules
"Als je tijd over hebt" = niet bestaan
Acceptance Criteria
Tests passen (specificeer welke)
Browser proof voor UI
Geen regressies (diff review)
EVIDENCE_LOG.md updated

## Slide 20
03.
Coding-Agent Prompt Template
You are the coding agent for this repository. Use the StateDD workflow.
Read first:
1. AGENTS.md 2. STATUS.md 3. PROJECT_STATE.yaml
4. PROJECT_DNA.yaml 5. NEXT_ACTIONS.md 6. BACKLOG.md 7. EVIDENCE_LOG.md
Task: Implement only <BL-ID>: <title>
Scope: ... Out of scope: ...
Acceptance criteria: ...
Subagent/tooling expectations:
- Implementation pass for code changes
- Verification pass for tests and failures
- Browser/tool-based verification for user-visible changes
- Evidence/documentation pass to create a proof bundle
- Do not self-approve. Prepare handoff for CTO review.
Proof bundle folder: docs/evidence/session-<next>-<bl-id>-<title>/
00-HANDOFF.md | 01-PROOF_MANIFEST.yaml | 02-SCOPE.md | 03-CHANGED_FILES.md
04-TEST_RESULTS.md | 05-BROWSER_PROOF.md | 06-GIT_STATUS.txt
07-KNOWN_LIMITATIONS.md | screenshots/ | logs/
Closure gates: No unrelated changes. No claim without proof.
Tests run and documented. User-visible changes need browser proof.
Runtime identity proven. State docs updated. Worktree clean.
Final handoff points to the proof bundle.

## Slide 21
03.
Final Handoff Structuur
Elke sessie eindigt met een paste-ready handoff:
## Handoff: <BL-ID> — <title>
### Wat veranderd
- File X: beschrijving van wijziging
- File Y: beschrijving van wijziging
### Wat direct geverifieerd
- Test X: resultaat
- Browser: URL + screenshot ref
### Identiteit
- Repo: <path> | Branch: <name> | HEAD: <commit>
- Process: <pid/container> | Endpoint: <url>
- Rebuild: <status> | Worktree: <clean/dirty>
### Evidence
- Bundle: docs/evidence/session-<n>-<bl-id>/
- Key artifacts: ...
### Known limitations
- ...
### Next recommended action
- <BL-ID>: <title>

## Slide 22
03.
Closure Gates
1. No unrelated changes in diff
2. No completion claim without proof
3. Tests run and results documented
4. User-visible changes have browser proof
5. Runtime identity proven (repo, branch, HEAD, endpoint)
6. State docs updated (PROJECT_STATE.yaml, STATUS.md, NEXT_ACTIONS.md)
7. Worktree clean at handoff
8. Final handoff points to proof bundle
Niet alles hoeft groen te zijn. Sommige gates kunnen "N/A" zijn.
Maar elke gate moet expliciet beantwoord zijn — geen "eh, vast wel".

## Slide 23
04.
Subagents, MCP & Tool Orchestration
Waarom één agent niet alles zelf mag doen

## Slide 24
04.
Het Probleem met de Alles-in-Één Agent
"Alsof een aannemer zijn eigen bouwvergunning, inspectie en opleveringsrapport schrijft."
Eén agent die zelf:
Requirements interpreteert
Code schrijft
Test
Bewijs maakt
Zichzelf goedkeurt
= Te veel macht, te weinig controle.
De agent kan niet objectief zijn over eigen werk. De agent kan niet tegelijk bouwen en beoordelen. De agent heeft geen externe verificatie nodig.

## Slide 25
04.
Subagents als Separation of Concerns
Human / Product Owner
↓
CTO / Orchestrator Agent
↓
• Coding Agent → bouwt
• Test Agent → verifieert
• Evidence Agent → documenteert bewijs
• Documentation Agent → bijwerkt state files
• Review / CTO Agent → beoordeelt
↓
StateDD Files + Proof Bundle
Key principe: Geen agent beoordeelt eigen werk.

## Slide 26
04.
Per Rol: Wat, Tools, Wat Niet
Coding Agent
Wat: Implementeert backlog items
Tools: Filesystem MCP, Terminal MCP, Git MCP
Wat niet: Zelf goedkeuren, scope veranderen
Test Agent
Wat: Verifieert testresultaten, checkt regressies
Tools: Terminal MCP, Filesystem MCP
Wat niet: Code wijzigen, testen negeren
Evidence Agent
Wat: Maakt screenshots, logs, artifacts
Tools: Browser/CDP MCP, Screenshot tools
Wat niet: Bewijs vervalsen, context weglaten
Documentation Agent
Wat: Werkt state files bij
Tools: Filesystem MCP, Git MCP
Wat niet: Truth verzinnen, files out-of-sync
Review / CTO Agent
Wat: Beoordeelt handoff + proof bundle
Tools: Filesystem MCP, Git MCP
Wat niet: Zelf code schrijven, review overslaan

## Slide 27
04.
MCP Servers als Gereedschapslaag
Niet:
Agent denkt → Agent antwoordt
(hallucinatie risico)
Wel:
Agent denkt → Agent gebruikt tool
→ Agent ziet echte output
→ Agent beslist volgende stap
MCP = Model Context Protocol
• Standaardprotocol voor agents om tools aan te roepen
• Tools geven echte, verifieerbare output
• Agent kan niet meer "gissen" over repo state

## Slide 28
04.
Praktische MCP Types
Filesystem MCP
Repo en state files lezen/schrijven
Git MCP
Status, diff, branch, commit, clean worktree
Terminal MCP
Tests, linters, builds, typecheck
Browser/CDP MCP
Echte UI-verificatie, form submits, clicks
Screenshot/Video
Visueel bewijs van UI states
Database MCP
Schema check, data validatie, queries
Issue Tracker MCP
Backlog koppelen aan tickets (Jira, GitHub)
Docs/Export
Proof documenten genereren, PDF export
Secrets Scanner
Voorkomen dat bewijs gevoelige data lekt

## Slide 29
04.
MCP Risico's & Controles
Risico's
MCP verhoogt agent capaciteit = meer schade bij fout
Agent kan per ongeluk files deleten
Agent kan database aanpassen
Agent kan gevoelige data in logs schrijven
Te veel tools = te veel macht
Controles
Scope grenzen: welke tools, welke paden, read vs write
Permissies: read-only voor productie data
Closure gates: verificatie verplicht na tool gebruik
Bewijsregels: elke tool-actie moet gelogd worden
Separation: coding agent heeft niet alles, review agent heeft leesrecht

## Slide 30
04.
Demo: Multi-Agent Flow met Tools
1
CTO Agent (planning chat)
Bepaalt volgende slice: BL-012. Schrijft scope + acceptance criteria. Delegeert aan coding agent.
2
Coding Agent (repo sessie)
Leest state files. Implementeert via filesystem + terminal MCP. Maakt proof bundle. Bereidt handoff voor.
3
Test Agent (verificatie)
Run tests via terminal MCP. Checkt regressies via git diff. Logt resultaten.
4
Evidence Agent (documentatie)
Screenshots via browser MCP. Verzamelt logs. Maakt proof manifest.
5
Review / CTO Agent (beoordeling)
Leest handoff + proof bundle. Beoordeelt: ACCEPTED / CONDITIONAL / REJECTED. Geeft next action.

## Slide 31
05.
Proof Bundles & CTO Review
"No proof, no closure"

## Slide 32
05.
Chat Claim vs Proof Bundle
Chat Claim
"Het werkt nu" → verdwijnt bij nieuwe sessie
Geen reproduceerbaarheid
Geen versioning
Geen audit trail
Alleen de agent die chatte weet het
Proof Bundle
Genummerde folder: session-001-bl-012-login/
Bewijst specifieke claim met artifacts
Git-tracked
Reviewbaar door mens of agent
Overdraagbaar tussen sessies

## Slide 33
05.
Proof Bundle Folderstructuur
docs/evidence/
session-001-bl-012-login-validation/
00-HANDOFF.md ← Wat is er gebeurd
01-PROOF_MANIFEST.yaml ← Metadata en verificatie status
02-SCOPE.md ← Wat was de opdracht
03-CHANGED_FILES.md ← Welke files gewijzigd
04-TEST_RESULTS.md ← Test output
05-BROWSER_PROOF.md ← UI verificatie
06-GIT_STATUS.txt ← Git state
07-KNOWN_LIMITATIONS.md ← Eerlijke known issues
screenshots/
001-login-empty-error.png
002-login-invalid-email.png
logs/
typecheck.log
unit-tests.log
browser-console.log
artifacts/

## Slide 34
05.
Per Bestand: Wie, Wat, Waarom

## Slide 35
05.
Proof Manifest Template
proof_bundle:
session: "session-001"
backlog_item: "BL-012"
title: "login-validation"
created_at: "YYYY-MM-DD"
repo:
path: ""
branch: ""
head: ""
worktree_status: ""
runtime:
base_url: ""
process_or_container: ""
runtime_head: ""
verification:
typecheck: "pass | fail | not_run"
unit_tests: "pass | fail | not_run"
lint: "pass | fail | not_run"
browser_proof: "pass | fail | not_applicable"
artifacts:
screenshots: []
logs: []
known_limitations: []
closure_recommendation: "accepted | conditional | rejected"

## Slide 36
05.
CTO-Review Prompt Template
You are the CTO/reviewer agent.
Review the coding agent handoff and the attached proof bundle.
Do not assume the work is complete because the coding agent says so.
Check:
1. Does the handoff match the requested backlog item?
2. Are there unrelated changes?
3. Are acceptance criteria explicitly verified?
4. Are test results included?
5. Is browser proof included for user-visible changes?
6. Is runtime identity proven?
7. Is the evidence folder correctly numbered and complete?
8. Is git status clean?
9. Are known limitations honestly documented?
10. Are state files updated?
11. Is the next recommended action logical?
Return one of: ACCEPTED | CONDITIONALLY ACCEPTED | REJECTED
Include: reasoning, missing evidence, risks, follow-up prompt

## Slide 37
05.
"No Proof, No Closure"
Geen bewijs = geen closure.
Geen closure = geen volgende action.
Geen volgende action = geen progress.
De gouden regels:
Een claim zonder bewijs is een hallucinatie
Een handoff zonder proof bundle is een chatlog
Een review zonder checklist is een rubber stamp
Een sessie zonder state update is verloren werk
Dit is geen bureaucratie.
Dit is hoe je fake progress eliminert.

## Slide 38
06.
Workshop & Maturity
Van niveau 0 naar niveau 7

## Slide 39
06.
Maturity Ladder
0 Losse prompts — "Fix dit even"
1 Betere prompts — "Lees deze files eerst"
2 State files — AGENTS.md + STATUS.md
3 Backlog + next actions — BL-001 + NEXT_ACTIONS.md
4 Evidence + runtime proof — EVIDENCE_LOG.md + identity
5 Subagents + MCP tooling — Coding + test + evidence agents
6 Proof bundles + CTO review — Genummerde bundles + review gate
7 Team workflow — Gedeelde state, peer review, adoptie

## Slide 40
06.
Halve-Dag Workshop
1
Fork/clone StateDD_Template
2
Initialiseer een nieuw project
3
Schrijf een realistisch AGENTS.md voor een project dat je kent
4
Vul STATUS.md + PROJECT_STATE.yaml in
5
Maak een BACKLOG.md met 3 items
6
Schrijf een NEXT_ACTIONS.md met 1 actief item
7
Schrijf 1 coding-agent prompt met scope + acceptance criteria
Tijd: 15 minuten
Deel met je buurman/buurvrouw: wat mist er nog?

## Slide 41
06.
Hele-Dag Workshop Outputs
Elke deelnemer heeft op het einde:
[ ] Mini AGENTS.md (voor jouw project)
[ ] Mini PROJECT_STATE.yaml (huidige truth)
[ ] 3 backlog items in BACKLOG.md
[ ] 1 NEXT_ACTION met scope + exit criteria
[ ] 1 coding-agent prompt (volledig template)
[ ] 1 proof bundle contract (folderstructuur + manifest)
[ ] 1 CTO-review prompt (11-punten checklist)
[ ] Peer-reviewed verbeterpunten
[ ] Team adoptie plan (niveau 0 → jouw niveau)
Tijd: 3 uur (inclusief peer review)

## Slide 42
06.
Peer Review Moment
In duo's van 2:
1
Wissel AGENTS.md en coding-agent prompt uit
2
Beoordeel elkaars prompt met de CTO-review checklist
3
Geef feedback op:
scope scherp? criteria meetbaar? closure gate mist? bundle compleet?
4
Verbeter je eigen prompt op basis van feedback
5
Deel 1 leerpunt met de hele groep
Tijd: 20 minuten

## Slide 43
06.
Wat Je Morgen Kan Doen
Start elke sessie met "Lees eerst AGENTS.md"
30 seconden, enorme impact
Houd NEXT_ACTIONS.md kort
Max 10, alleen actief, met exit criteria
Eis runtime identity proof
Repo + branch + HEAD + endpoint, altijd
Gebruik scope + out-of-scope
In elke prompt, expliciet
Scheid coding van review
Nooit dezelfde agent die bouwt én goedkeurt
Begin met proof bundles
Ook klein: 1 folder, 1 screenshot, 1 log
Kies er één. Doe die één week consistent. Dan pas de volgende.

## Slide 44
StateDD: Discipline > Hype
github.com/lennertvhoy/StateDD_Template
AI coding is krachtig, maar onbetrouwbaar zonder workflow
De echte vijand is ontbrekende projectwaarheid
StateDD maakt de repo de bron van waarheid
Agents krijgen rollen, geen absolute macht
Tools bewijzen, bundles overdragen, CTO beoordeelt
Begin vandaag met niveau 1 of 2
Vragen?
Open source, MIT licensed. Gebruik het, fork het, verbeter het.
