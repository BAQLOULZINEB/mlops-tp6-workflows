"""TP6 - planifier.py

ROLE      : Cree le deploiement 'hebdomadaire' (chaque lundi 6 h) et reste a l'ecoute pour executer les runs.
ENTREE    : le flow reentrainement de flow_mlops.py
SORTIE    : deploiement reentrainement-fraude/hebdomadaire dans Prefect
A RETENIR : serve = deploiement + executeur dans le meme processus : si on l'arrete, les runs restent en attente (Late).
"""

from flow_mlops import reentrainement

if __name__ == '__main__':
    # Cree le deploiement "hebdomadaire" puis attend les executions a lancer.
    # Laisser ce terminal ouvert ; Ctrl + C pour arreter.
    reentrainement.serve(name='hebdomadaire',
                         cron='0 6 * * 1')          # chaque lundi a 6 h
