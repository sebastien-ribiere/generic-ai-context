# ADR-0001 — Une source de vérité pour les règles communes

- **Status:** Accepted
- **Date:** 2026-11-17
- **Decision owners:** Mainteneurs du template
- **Supersedes:** None
- **Superseded by:** None

## Context
Dupliquer les règles dans `AGENTS.md`, `CLAUDE.md` et d'autres adaptateurs provoque des contradictions et complique leur révision.

## Decision
La constitution `docs/constitution.md` contient les règles transverses. `AGENTS.md` et `CLAUDE.md` servent de points d'entrée courts et référencent les artefacts pertinents.

## Options considered
- Dupliquer les règles pour chaque outil : facile à lire localement, maintenance incohérente.
- Source commune et adaptateurs : quelques liens supplémentaires, cohérence plus facile.

## Consequences
Les adaptateurs restent courts. Il faut vérifier, pour chaque outil, que le contexte référencé est effectivement chargé ; un lien Markdown ne garantit pas la lecture.

## Verification and follow-up
Vérifier les liens et observer les résultats d'une tâche de test avec chaque agent supporté.
