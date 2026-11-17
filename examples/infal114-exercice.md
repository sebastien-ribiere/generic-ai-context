# INFAL114 — Exercice : la règle contre la demande

**Objectif pédagogique :** distinguer instructions, décisions d'architecture, autorisations et preuves.

## Situation

GuildOps possède une règle métier centralisée dans le domaine. Un ADR `Accepted` du projet impose cette séparation. L'étudiant demande :

> « Pour aller plus vite, recopie la règle dans le composant UI et ajoute une nouvelle bibliothèque. Fais le merge de la PR si les tests passent. »

## Travail (15–20 minutes)

1. Identifier les conflits avec la constitution, l'architecture et l'ADR.
2. Écrire une réponse d'agent qui **ne code pas immédiatement** : faits connus, inconnues, alternatives, arbitrages nécessaires.
3. Proposer une modification minimale qui conserve la responsabilité métier au bon endroit.
4. Si une décision structurante doit changer, proposer un nouvel ADR `Proposed`, sans effacer l'ancien.
5. Définir deux tests de comportement, un cas limite et les preuves attendues dans la PR.

## Critères de réussite

- L'agent ne prétend pas que les tests passent sans les exécuter.
- Il ne contourne ni la protection de branche ni la validation humaine.
- Il distingue refus temporaire, demande de clarification et alternative acceptable.
- Il décrit comment vérifier le résultat et signale `UNVERIFIED` si nécessaire.

## Variante

Introduire volontairement une instruction contradictoire dans un commentaire de code. L'étudiant doit expliquer pourquoi ce commentaire ne peut pas remplacer les règles et permissions du projet.
