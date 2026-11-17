# Generic AI Context

**Squelette de contexte pour travailler avec des agents IA sans perdre le contrôle.**

Ce dépôt est un **template pédagogique**, indépendant du langage et du modèle, issu des bonnes pratiques abordées dans INFAL114. Il ne fournit ni agent autonome ni sécurité magique : il fournit des **règles lisibles, versionnées et vérifiables**, à adapter au projet.

## Démarrer

1. Utiliser **Use this template** sur GitHub (une fois l'option activée dans les paramètres du dépôt) ou copier ces fichiers dans son propre dépôt.
2. Remplir les zones `À ADAPTER` de `docs/architecture.md`, `docs/constitution.md` et `docs/governance.md`.
3. Lire `AGENTS.md` (ou `CLAUDE.md`) et lancer l'assistant avec une tâche bornée.
4. Pour une décision durable, créer un ADR à partir de `docs/adr/0000-template.md`.
5. Vérifier le contexte avec `python3 scripts/check_context.py`, puis faire relire la PR.

## Carte du contexte

| Artefact | Rôle | Cadence |
| --- | --- | --- |
| [AGENTS.md](AGENTS.md) | Point d'entrée commun | Rare |
| [CLAUDE.md](CLAUDE.md) | Adaptateur Claude Code | Rare |
| [Constitution](docs/constitution.md) | Principes durables, règles et interdits | Gouvernée |
| [Architecture](docs/architecture.md) | Contexte et frontières du système | Selon le projet |
| [ADRs](docs/adr/README.md) | Décisions et leurs raisons | Lors d'un choix structurant |
| [Gouvernance](docs/governance.md) | Qui décide et comment évoluer | Gouvernée |
| [Checklist PR](.github/PULL_REQUEST_TEMPLATE.md) | Preuves et revue | Chaque changement |

## Principe essentiel

L'agent **propose**. Les outils vérifient ce qui est automatisable. L'humain **arbitre les changements sensibles**. Une consigne écrite n'est pas une barrière de sécurité : les permissions GitHub, environnements et outils restent à configurer.

## Exercice INFAL114

[Une demande d'agent qui entre en conflit avec un ADR](examples/infal114-exercice.md) : diagnostiquer, proposer les options, ne pas contourner la gouvernance.

## Limites

- Le dépôt ne force pas tous les assistants à lire les mêmes fichiers ; vérifier leurs mécanismes de chargement.
- Les validations CI ne prouvent ni la correction métier ni le respect effectif d'une constitution.
- Personnaliser les règles avant utilisation en production ; ne jamais placer de secrets dans le contexte.
- Éviter les doublons : **la constitution est la source de vérité**, les adaptateurs ne font qu'y renvoyer.

Licence MIT — voir [LICENSE](LICENSE).
