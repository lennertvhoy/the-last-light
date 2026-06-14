# AI-Driven Development — Prompt-Copy Website Generator

Dit kleine script genereert de workshop-promptenpagina binnen de bestaande
Docsify-site van *The Last Light*.

## Bestanden

- `prompt-index.yaml` — metadata voor de 9 verplichte prompts (slug, titel, fase,
  CLI/GUI-notitie, screenshot-momenten).
- `generate.py` — leest de canonieke prompts uit `prompts/` en schrijft:
  - `docs/ai-driven-dev/prompts/README.md`
  - `docs/ai-driven-dev/prompts/_sidebar.md`
  - `docs/ai-driven-dev/prompts/one-pager.md`
- `test_generate.py` — basis-tests die controleren of alle prompts leesbaar zijn
  en de gegenereerde bestanden de verwachte slugs bevatten.

## Gebruik

Vanuit de repo-root:

```bash
python3 g.Presentations/workspaces/ai-driven-dev-rework/prompt-website/generate.py
```

Om te controleren of de gegenereerde bestanden nog overeenkomen met de
gecommitte versies (bijv. in CI):

```bash
python3 g.Presentations/workspaces/ai-driven-dev-rework/prompt-website/generate.py --check
```

## Wanneer opnieuw genereren?

- Na elke wijziging in `prompts/`.
- Voor elke cursus-aflevering.
- Na wijzigingen in `prompt-index.yaml`.

## UI-taal

De interface van de prompt-site is in het Nederlands, zoals vastgelegd in
`DESIGN_DECISIONS.md`. De canonieke prompts zelf blijven Engelstalig.
