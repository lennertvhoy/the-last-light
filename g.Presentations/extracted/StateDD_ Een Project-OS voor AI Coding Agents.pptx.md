# StateDD_ Een Project-OS voor AI Coding Agents

Source: `/home/ff/Documents/Projects/the-last-light/g.Presentations/curated/StateDD_ Een Project-OS voor AI Coding Agents.pptx`
Slides: 28

## Slide 1
StateDD
Een Project-OS voor AI Coding Agents
Hoe je context decay, fake progress en chaotische agent-sessies voorkomt

## Slide 2
Wat gaan we bespreken?
01
Het Probleem
Waarom AI agents ontsporen
02
StateDD als Oplossing
Het template en de files
03
Workflow in de Praktijk
Van bootstrap tot handoff
04
Agents & Tools
Claude, Codex, Cursor, Kimi, OpenCode
05
Mini-Workshop
Zelf aan de slag

## Slide 3
01.
Het Probleem
Waarom AI coding agents vaak ontsporen

## Slide 4
01.
Waarom AI coding agents ontsporen
AI agents hebben geen persistent geheugen tussen sessies
Elke nieuwe sessie begint blind — ze "vergeten" wat ze net bouwden
Ze halucineren file structuren die niet bestaan
Ze claimen "klaar" terwijl de code niet compileert
Ze overschrijven werkende code zonder het te testen

## Slide 5
01.
Context Decay
Schone Start
Volledige context beschikbaar. Agent begrijpt het project.
Context Verlies
Na ~10-20 prompts raakt de agent het overzicht kwijt.
Chaos
Broken assumptions. Fake progress.
Context decay = het proces waarbij een AI agent zijn grip op de projectrealiteit verliest
De chat window wordt de enige bron van waarheid — maar die is vluchtig
Belangrijke beslissingen verdwijnen in chat history. De repo loopt uit de pas met de runtime.

## Slide 6
01.
"Klaar" is niet hetzelfde als bewezen
✗ Wat we vaak zien
"Het werkt nu" = geen bewijs
Screenshots zonder runtime identity
Niet gecompileerd / niet getest
"Ik heb het bestand aangepast" = waarheid?
✓ Wat StateDD vraagt
Directe verificatie verplicht
Runtime identity proof: repo, branch, HEAD, endpoint
Screenshots gekoppeld aan specifieke claims
Alleen geaccepteerd na acceptance freeze

## Slide 7
02.
StateDD als Oplossing
Een project-OS tegen context decay

## Slide 8
02.
Wat is StateDD?
StateDD = State Driven Development Template
Geeft mensen en coding agents een gedeelde bron van waarheid in de repo
Live state, korte active queue, bewijs voor claims, clean handoffs
Voor projecten die meer discipline willen dan ad-hoc prompting
Zonder de repo te veranderen in "process theater"
Open source: github.com/lennertvhoy/StateDD_Template

## Slide 9
02.
De StateDD Files
AGENTS.md
Operating contract en repo-mode regels voor elke agent
STATUS.md
Korte human snapshot van huidige waarheid
PROJECT_STATE.yaml
Machine-checkable current truth
PROJECT_DNA.yaml
Stable architecture and governance contract
NEXT_ACTIONS.md
Active queue alleen — max 10 items
BACKLOG.md
Medium-term roadmap met stable IDs

## Slide 10
02.
AGENTS.md — Het Operating Contract
Dit is het eerste bestand dat elke agent moet lezen. Het definieert repo mode (bootstrap vs operating) en bevat universele regels die elke sessie moet volgen.
AGENTS.md — Universele Regels
● No fake completeness — "klaar" = bewezen, niet geclaimd
● No unverified claims presented as fact
● User-facing behavior requires direct verification
● Negative searches stay negative
● Active queue stays short (max 10 items)
● Coding agent standaard: lees AGENTS.md eerst, anker op verified truth
Repo mode: bootstrap = discovery fase, scheid facts van assumptions. operating = delivery fase, execute backlog slices.

## Slide 11
02.
PROJECT_STATE.yaml — Machine-Checkable Truth
Structured current truth in YAML. Niet voor menselijke prose — voor precieze feiten. Altijd updaten na elke sessie waar truth verandert.
PROJECT_STATE.yaml — Voorbeeld
# Workflow state
workflow:
repo_mode: bootstrap
bootstrap:
completed: false
system_investigated: false
# Runtime identity
runtime_identity:
status: unknown
Verification labels: observed | unknown | reported | blocked | assumed | stale | invalid

## Slide 12
02.
NEXT_ACTIONS.md + BACKLOG.md — Queue Discipline
NEXT_ACTIONS.md
Active execution queue
Max 10 items
Alleen open, actief werk
Elke item verwijst naar backlog ID [BL-001]
Owner + next action + exit criteria
Remove completed items immediately
BACKLOG.md
Strategic roadmap
Stable backlog IDs (BL-001, BL-002...)
NOW / NEXT / LATER / WATCHLIST
WATCHLIST bewaakt: queue bloat, unverified claims, premature operating-mode transition

## Slide 13
02.
EVIDENCE_LOG.md — Bewijs, geen claims
Structured ledger of proof artifacts. Elke user-facing claim heeft bewijs nodig. Bewaar artifacts onder docs/evidence/YYYY-MM-DD-slug/
EVIDENCE_LOG.md — Entry Format
id: EV-2026-08-05-001
file: /docs/evidence/2026-08-05-login/test-passed.png
source: test # browser | api | test | log
action: Implemented email validation on UserService
shows: 3/3 tests passing, screenshot attached
proves: User-facing validation works as specified in BL-003
"Klaar" zonder bewijs is fake progress. EVIDENCE_LOG.md maakt het expliciet: je claimt iets, je bewijst het.

## Slide 14
03.
Workflow in de Praktijk
Van bootstrap tot handoff

## Slide 15
03.
De StateDD Workflow Loop
Plan + Handoff via CTO chat | Coding agent doet Execute + Record
Bootstrap
Onderzoek repo, scheid facts van assumptions, bouw baseline
Plan
Kies één kleine next slice uit de backlog
Execute
Implementeer en verifieer direct
Record
Update state en evidence wanneer truth verandert
Handoff
Laat de volgende sessie een duidelijk startpunt
Scheiding: CTO chat bepaalt de volgende slice → Coding agent voert uit en update repo truth
Nooit beide in één sessie.

## Slide 16
03.
Slecht vs Goed Prompting
Slecht
"Fix de bug"
"Maak een login pagina"
"Refactor de hele app"
Agent editeert voor het lezen van state files
Geen verificatie, geen evidence
Goed (StateDD-style)
"Lees AGENTS.md, STATUS.md, PROJECT_STATE.yaml, NEXT_ACTIONS.md"
"Implementeer [BL-003]: email validatie. Scope: UserService.java + test."
"Verifieer: run tests, screenshot resultaat, update EVIDENCE_LOG.md"
"Eindig met handoff: wat veranderd, wat bewezen, next action"

## Slide 17
03.
Runtime Identity Proof
Voordat je user-facing gedrag accepteert, check dit:
Welke repo? → canonical path
Welke branch? → branch name
Welke commit? → HEAD
Welk process/container? → runtime identity
Welke endpoint? → port/base_url
Is de artifact rebuilt? → rebuild status
Zijn er duplicate runtimes? → checked
Pro Tip
Gebruik prompts/RUNTIME_IDENTITY_CHECKLIST.md
Screenshots alleen nadat je bewezen hebt welke runtime actief was.
Classic mistake: localhost:3000 in screenshot, maar agent draait op :3001 — je test de verkeerde runtime

## Slide 18
03.
Handoffs & Clean Worktrees
Elke sessie eindigt met een handoff:
Wat er veranderd is
Wat direct geverifieerd is
Repo path, branch, git HEAD
Process/container, endpoint
Rebuild status, clean worktree
Evidence references
Next recommended action
Handoff wording is paste-ready voor de CTO chat
Gebruik prompts/FINAL_HANDOFF_TEMPLATE.md
Handoff Template
Wat veranderd:
• [Lijst van gewijzigde files]
Wat geverifieerd:
• [Test resultaten, build status]
Runtime identity:
• Repo: [path] | Branch: [name]
• HEAD: [commit hash]
• Endpoint: [url:port]
Evidence:
• [EV-YYYY-MM-DD-001]
Next action:
• [Aanbevolen vervolgstap]

## Slide 19
03.
StateDD voor Teams, niet alleen solo
StateDD schaalt naar teams
Gedeelde repo truth = gedeeld begrip
BACKLOG.md = gedeelde roadmap
WORKLOG.md = append-only geschiedenis
EVIDENCE_LOG.md = audit trail
Multi-agent setup
CTO agent (planning) — scoping, prioritering
Coding agent (repo) — implementatie, verificatie
Human — beslissingen, paste handoffs, acceptatie
Geen "ik heb het gisteren gedaan" meer — het staat in de repo

## Slide 20
04.
Agents & Tools
Claude Code, Codex, Cursor, Kimi, OpenCode

## Slide 21
04.
StateDD + Jouw Coding Agent
Claude Code
Uitstekend. Leest hele repos, volgt instructies. Start met CODING_AGENT_STARTUP_PROMPT.md
Codex (OpenAI)
Sterk. StateDD files passen in context window. Gebruik CTO_SESSION_PROMPT voor planning.
Cursor
Goed. Composer mode + StateDD files = duidelijke context. .cursorrules kan verwijzen naar AGENTS.md.
Kimi
Werkt. Chinese + internationale support. Zelfde startup prompt flow.
OpenCode / Aider
Directe integratie. CLI tools die StateDD files als context kunnen consumeren.
Alle tools: start met AGENTS.md → STATUS.md → PROJECT_STATE.yaml → NEXT_ACTIONS.md

## Slide 22
04.
Demo: StateDD in Actie
1
Init template
python3 scripts/init_template.py \
new --name "MijnProject"
2
Start agent
Start agent met startup prompt: lees AGENTS.md eerst
3
Lees state files
Agent leest AGENTS.md, STATUS.md, PROJECT_STATE.yaml
4
Strategische vragen
Agent vraagt strategische vragen (bootstrap mode)
5
Slice → verify → handoff
Eerste implementatie slice → verificatie → handoff
[Dit is het demo moment. Laat een korte sessie zien waarbij je een nieuw repo initialiseert en de agent door de bootstrap fase leidt.]

## Slide 23
05.
Mini-Workshop
Zelf een AI agent aansturen met StateDD

## Slide 24
05.
Workshop Opdracht
15 min
1
Fork/clone StateDD_Template
2
Initialiseer een nieuw project met init_template.py
3
Schrijf een realistisch AGENTS.md voor een project dat je kent
4
Vul STATUS.md en PROJECT_STATE.yaml in
5
Maak een BACKLOG.md met 3 echte backlog items
6
Schrijf een NEXT_ACTIONS.md met 1 actief item
7
Simuleer een handoff: wat zou je plakken in de CTO chat?
Tip
Geen perfectie nodig. Het doel is dat je de files een keer hebt aangeraakt en begrijpt waar ze voor dienen. De meeste mensen leren StateDD pas echt als ze het zelf doen.

## Slide 25
05.
Wat je morgen al kan toepassen
1
Start elke agent-sessie met "Lees eerst AGENTS.md"
2
Houd NEXT_ACTIONS.md kort — max 10 items, alleen actief werk
3
Eis runtime identity proof voor elke "het werkt" claim
4
Update PROJECT_STATE.yaml als truth verandert
5
Eindig elke sessie met een paste-ready handoff
6
Scheiding: CTO chat voor planning, coding agent voor executie

## Slide 26
StateDD: Discipline > Hype
github.com/lennertvhoy/StateDD_Template
StateDD is geen magic bullet
Het is een discipline die je projecten betrouwbaarder maakt
AI coding werkt pas echt goed met duidelijke state
De repo is de bron van waarheid — niet de chat
Open source, MIT licensed. Gebruik het, fork het, verbeter het.

## Slide 27
Vragen?
Laten we het bespreken
github.com/lennertvhoy/StateDD_Template
Stel je vraag — technisch, strategisch, of praktisch
Technische details, adoptie-strategie, team roll-out

## Slide 28
05.
Dieper Inzicht: Bootstrap vs Operating
Bootstrap
Discovery fase
Scheid observed facts van assumptions
Vul STATUS.md met waarheid, niet met wensen
Project DNA nog niet stabiel
Gate: check_state_docs.py --bootstrap-gate
Operating
Delivery fase
Backlog slices uitvoeren
Updates aan state files bij elke verandering
Acceptance freezes na milestones
Hygiene check voor elke handoff
Waarschuwing: Veel teams willen te snel naar operating mode. Een leugenaar in bootstrap wordt een leugenaar in operating.
