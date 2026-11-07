"""TP6 - verifier_qualite.py

ROLE      : La regle de qualite pour GitHub Actions : sort avec le code 1 si F1 < seuil.
ENTREE    : reports/metrics.json + params.yaml
SORTIE    : affichage OK / ECHEC + code de sortie 0 ou 1
A RETENIR : Code 1 = etape rouge dans GitHub Actions : le commit est marque en echec.
"""

import sys
import json
import yaml

with open('reports/metrics.json', encoding='utf-8') as f:
    f1 = json.load(f)['f1']
with open('params.yaml', encoding='utf-8') as f:
    seuil = yaml.safe_load(f)['validation']['seuil_f1']

print(f'F1 = {f1} | seuil = {seuil}')
if f1 < seuil:
    print('ECHEC : modele refuse')
    sys.exit(1)                  # code 1 = etape rouge dans GitHub Actions
print('OK : modele accepte')
