# TP06 - Automatiser les workflows MLOps (Prefect + GitHub Actions)

Fiche explicative : `EXPLICATION_TP6.html` | Rapport : `rapport_tp6.md`

```powershell
.venv\Scripts\Activate.ps1
# terminal 1
prefect server start                     # http://127.0.0.1:4200
# terminal 2
prefect config set PREFECT_API_URL=http://127.0.0.1:4200/api
dvc pull
python flow_mlops.py                     # le workflow en 4 taches
python verifier_qualite.py               # la regle de qualite de la CI
# terminal 3
python planifier.py                      # planification hebdomadaire (serve)
prefect worker start --pool pool-tp      # ou : worker du work pool
```
