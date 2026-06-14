# The Last Light: How to Stay Human When Everything Can Be Outsourced

![Project Status](https://img.shields.io/badge/status-in%20progress-blue.svg)
![License](https://img.shields.io/badge/license-MIT%2FCC%20BY--SA%204.0-lightgrey.svg)

## Project Description

**The Last Light** is an open-source book about AI, agency, and *conscious delegation*: the discipline of knowing what to hand over to machines, what to keep, and how to decide.

The manuscript argues that human consciousness is not being replaced so much as tested. The danger is not the tools themselves, but the unconscious drift toward outsourcing the very capacities that make us human. The book offers a practical field guide for individuals, educators, and organizations who want to use AI without becoming it.

## A Note on Irony

I am acutely aware of the irony inherent in creating a work that warns about the dangers of AI while simultaneously working with AI tools to develop it. This paradox is central to the questions this book seeks to explore. The tools we use to examine our predicament are themselves part of that predicament, and this recursive relationship is precisely what makes our current moment so unprecedented and urgent.

## Work in Progress

This manuscript is a work in progress. Rather than claiming certainty, the book aims to raise critical questions and provoke deeper thinking about our digital future. Feedback, corrections, and constructive criticism are welcome.

## Table of Contents

* [Project Description](#project-description)
* [Repository Structure](#repository-structure)
* [Getting Started: How to Read the Book](#getting-started-how-to-read-the-book)
* [State Driven Development Workflow](#state-driven-development-workflow)
* [Contributing](#contributing)
* [Authors and Acknowledgments](#authors-and-acknowledgments)
* [License](#license)

## Repository Structure

```
.
├── The-Last-Light.md              # Canonical author-ready manuscript
├── e.Combined-Book/               # Dated copies of the canonical manuscript
├── archive/legacy-manuscript/     # Previous 35-chapter manuscript
├── nl/                            # Legacy Dutch translation (stale)
├── index.html                     # Docsify entry point
├── _coverpage.md                  # Docsify cover page
├── _sidebar.md                    # Docsify navigation (auto-generated)
├── portia-theme.css               # Custom Docsify theme
├── f.Scripts/                     # Project-specific scripts
│   ├── generate-sidebar.py        # Generate _sidebar.md from The-Last-Light.md
│   └── combine-book.sh            # Create dated copies in e.Combined-Book/
├── scripts/                       # StateDD hygiene and audit scripts
│   ├── check_state_docs.py
│   ├── statedd_doctor.py
│   ├── statedd_audit.py
│   └── statedd_handoff.py
├── prompts/                       # StateDD prompt templates
├── docs/                          # StateDD evidence and acceptance logs
│   ├── EVIDENCE_LOG.md
│   ├── ACCEPTANCE_FREEZES.md
│   └── adr/
├── .github/
│   ├── workflows/                 # CI workflows (build, lint, test, statedd-validate)
│   ├── ISSUE_TEMPLATE/
│   └── pull_request_template.md
├── README.md                      # Public-facing repo overview
├── CONTRIBUTING.md                # Contribution guidelines
├── LICENSE                        # MIT (code) + CC BY-SA 4.0 (content)
└── package.json                   # docsify-cli, markdownlint-cli
```

## Getting Started: How to Read the Book

**Online:** Visit [lennertvhoy.github.io/the-last-light](https://lennertvhoy.github.io/the-last-light/).

**Locally:**

```bash
npm install
npx docsify serve .
```

Then open http://localhost:3000.

## State Driven Development Workflow

This repository uses **State Driven Development (StateDD)** to keep project truth explicit and durable.

Coding agents should start every session by reading:

1. `AGENTS.md` — operating contract
2. `STATUS.md` — current snapshot
3. `PROJECT_STATE.yaml` — structured truth
4. `PROJECT_DNA.yaml` — stable architecture
5. `NEXT_ACTIONS.md` — active queue

Before claiming a slice is complete, run:

```bash
python3 scripts/check_state_docs.py
python3 scripts/statedd_doctor.py
```

For full closure-grade work, also run:

```bash
python3 scripts/statedd_audit.py
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## Authors and Acknowledgments

Written by Lennert Van Hoye. Contributions, critiques, and forks are welcome.

## License

- **Code** (scripts, CI, site configuration): MIT License
- **Book content** (manuscript Markdown files): Creative Commons Attribution-ShareAlike 4.0 International
