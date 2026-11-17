# Gouvernance des artefacts de contexte

## Autorité et cycle de modification

**À ADAPTER :** nommer le responsable technique, les reviewers et les éventuelles approbations obligatoires. Par défaut, les agents **proposent**, les humains **décident** ; les contrôles du dépôt et les permissions appliquent les limites.

| Artefact | Qui propose ? | Qui approuve ? | Déclencheur de révision |
| --- | --- | --- | --- |
| Constitution | Agent ou contributeur | Responsable humain désigné | Incident, règle inapplicable, retour d'expérience |
| Architecture | Contributeur | Responsable technique | Changement de frontières ou de système |
| ADR | Agent ou contributeur | Responsables concernés | Décision structurante ou contradiction |
| AGENTS.md / CLAUDE.md | Contributeur | Responsable du contexte | Évolution des outils ou de la navigation |

## Processus simple

1. **Proposer** par PR : besoin, diff, risques et dépendances.
2. **Évaluer** : compatibilité avec l'architecture et les ADR, impacts sur agents et humains.
3. **Vérifier** : lint du contexte, exemples, éventuellement un essai de tâche agentique.
4. **Approuver** par un humain autorisé ; ne pas laisser l'agent s'auto-approuver.
5. **Publier et observer** : lier la décision et relever les écarts réels.

## Conflits et priorité

Les permissions techniques, la sécurité et les politiques d'organisation ne sont jamais annulées par une instruction dans un fichier. Une tâche ne peut pas modifier silencieusement la constitution ou contredire un ADR `Accepted`. En cas de conflit : **arrêter la partie concernée, présenter les alternatives, demander décision**.

Une règle commune n'est définie qu'une fois : les fichiers d'entrée renvoient à la constitution. Éviter les copies divergentes.

## ADR : statuts et historique

- `Proposed` : discussion et alternatives en cours.
- `Accepted` : décision applicable, avec approbation tracée.
- `Rejected` : décision non retenue, conservée avec ses raisons.
- `Superseded` : décision remplacée par un **nouvel ADR**, avec lien bidirectionnel.

Ne pas réécrire une ancienne décision pour faire croire qu'elle a toujours été différente. Archiver ne signifie pas effacer. Vérifier régulièrement si les ADR acceptés sont encore appliqués.

## Definition of Done pour une modification de contexte

- Motivation et portée explicites
- Revue humaine identifiée
- Aucune contradiction non résolue entre fichiers
- Liens et statut ADR cohérents
- `python3 scripts/check_context.py` réussi
- Limites de vérification signalées
