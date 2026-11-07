# Orchestrateur ou integration continue ? (TP06)

| Critere                          | Prefect (orchestrateur)                                  | GitHub Actions (CI)                                         |
|----------------------------------|----------------------------------------------------------|-------------------------------------------------------------|
| Ce qui declenche l'execution     | une date (cron lundi 6 h), un Quick run dans l'interface, un evenement | un `git push` (ou le bouton Run workflow)          |
| Ou s'execute le traitement       | sur notre poste/serveur : process `serve` ou worker du work pool `pool-tp` | sur une machine Linux de GitHub, ephemere          |
| Qui surveille, et ou             | l'equipe data, dans l'interface Prefect (Runs, Deployments, Work Pools) | les developpeurs, dans l'onglet Actions et sur le commit |
| Ce qui se passe en cas d'echec   | la tache `valider` passe en Failed, `notifier` ne s'execute pas, 2 reessais sur `rejouer_pipeline` | l'etape passe au rouge (code 1), le commit est marque en echec |
| Type de tache adapte             | traitements recurrents et longs sur les vraies donnees (reentrainement) | verifications rapides du code a chaque modification |
| Ce qui est versionne dans Git    | `flow_mlops.py`, `planifier.py` (et `prefect.yaml` s'il existe) | `.github/workflows/ci.yml`, `verifier_qualite.py`, `requirements-ci.txt` |

## Conclusion (5 lignes)

La CI repond a "le CODE est-il toujours correct ?" a chaque push ; l'orchestrateur repond a "le TRAITEMENT a-t-il tourne et reussi ?" chaque lundi.
Les deux appliquent la meme regle de qualite (F1 >= 0.82, lue dans params.yaml) : un modele a F1 0.25 est arrete dans les deux cas.
La CI travaille sur des donnees regenerees (pas d'acces au stockage DVC) ; Prefect travaille sur les vraies donnees du poste.
Prefect apporte la planification, les reessais, l'historique des runs et la separation serveur / work pool / worker.
Ils sont complementaires : la CI protege l'entree du code, l'orchestrateur execute et surveille la production.
