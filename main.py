"""TO DO:
    - Rapport de simulation plus détaillé
    - Inciter à construire davantage
    - Grouper des types de ressources
    - Accélération et Ralentissement
    - Habitations
    - Tags, effets immédiats pour la production de ressources (comme l'énergie ou le cannibalisme)
    - Groupes d'ouvrier
    - Conditions initiales (bâtiments, etc.) et gestion des dépôts disponibles (pour les camps, les fermes et les mines)
"""

import config
from montecarlo import run
from import_data import load_projects
from project import Project

"""
import json
with open("data/projects.json") as f:
    raw = json.load(f)

"""

project_list = load_projects()

projects = [
    Project(
        id=p["id"],
        card=p["card"],
        name=p["name"],
        workers_required=p["workers_required"],
        requirements=p["requirements"],
        grants=p["grants"],
        inputs=p["inputs"],
        outputs=p["outputs"],
        tags=set(p["tags"])
    )
    for p in project_list
]

#Définit les ressources et ouvriers de départ
resources = {
    "NOURRITURE": 60,
    "BOIS": 60,
}
workers = 25

#Lancer la simulation
print("Launching simulation...")
stats = run(
    config.SIMULATIONS,
    resources,
    workers,
    projects
)

print(f"Success rate: {stats.success_rate:.2f}%")

for resource, values in stats.resources.items():
    print(resource, sum(values) / len(values))

for requirement, values in stats.requirements.items():
    print(requirement, sum(values) / config.SIMULATIONS)