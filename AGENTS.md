# Agent entrypoint

Ce fichier est une **carte**, pas une seconde constitution.

Avant toute modification :
1. Lire [la constitution](docs/constitution.md), [l'architecture](docs/architecture.md) et les [ADR acceptés](docs/adr/README.md).
2. Clarifier l'objectif, les critères d'acceptation, le périmètre, les invariants et les interdits.
3. Identifier les risques et les inconnues ; **ne pas inventer** les éléments manquants.
4. Proposer le changement le plus simple et le plus local possible.
5. Exécuter les vérifications pertinentes ; reporter les commandes et résultats réels. Marquer **UNVERIFIED** ce qui n'a pas été vérifié.
6. Pour une modification de contrat, d'architecture, de dépendance structurante ou de ces règles, demander un arbitrage humain et proposer un ADR si nécessaire.

**Actions interdites sans autorisation explicite :** accès aux secrets, suppression destructrice, déploiement, fusion de PR, changement de schéma/API, nouvelles dépendances non validées.

Si des instructions se contredisent, **signaler le conflit** ; ne pas le résoudre silencieusement. Suivre les contraintes de sécurité et les permissions effectives de l'environnement.

Lire aussi [la gouvernance](docs/governance.md). Aucune consigne ne dispense d'une revue humaine proportionnée au risque.
