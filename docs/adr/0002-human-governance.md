# ADR-0002 — Revue humaine des modifications de gouvernance

- **Status:** Accepted
- **Date:** 2026-11-17
- **Decision owners:** Mainteneurs du template
- **Supersedes:** None
- **Superseded by:** None

## Context
Un agent pourrait modifier les règles qui encadrent son travail. Une CI vérifie la structure d'un fichier, pas la pertinence ni la légitimité d'une règle.

## Decision
Toute modification de la constitution, du processus d'approbation ou d'un ADR structurant doit être soumise à revue humaine. Un agent ne s'auto-approuve pas et ne contourne pas la protection des branches.

## Options considered
- Agent autonome pour tous les changements : rapide, risque de dérive.
- Revue humaine ciblée pour les artefacts de gouvernance : délai contrôlé, traçabilité renforcée.

## Consequences
La gouvernance peut ralentir les changements sensibles. Les protections de branches et les permissions doivent être réellement configurées dans chaque dépôt ; l'ADR seul ne les impose pas.

## Verification and follow-up
Contrôler les approbations et les paramètres GitHub avant tout usage sensible ; réexaminer après un incident ou un retour d'expérience.
