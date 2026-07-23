from inventory import Inventory
from workers import Workers
from tag_handler import TAG_HANDLERS
import allocator
import config

class Settlement:

    def __init__(self, resources, worker_count, projects):

        self.inventory = Inventory(resources)
        self.workers = Workers(worker_count)
        self.projects = projects
        self.requirements = set()
        self.season="BRUINE"

    def apply_tags(self, phase, project):

        for tag in project.tags:
            handler = TAG_HANDLERS.get(tag, {}).get(phase)
            if handler:
                handler(project, self)

    def consume_food(self):

        return self.inventory.consume({
            "NOURRITURE": self.workers.available
        })

    def consume_fuel(self):

        return self.inventory.consume({
            "BOIS": self.workers.available
        })

    # Check available projects based on season
    def get_cycle_projects(self):
        output_projects = []
        for project in self.projects:
            if project.is_available(self):
                #print(f"Projet valide: {project.id}")
                output_projects.append(project)
        return output_projects

    def cycle(self, cycle):
        self.update_season(cycle)
        #print (f"Cycle {cycle}, saison {self.season}, ouvriers dispos {self.workers.available}, nourriture dispo {self.inventory.resources['NOURRITURE']}")

        local_projects = self.get_cycle_projects()

        assignments = allocator.allocate(
            local_projects,
            self.workers,
            self.inventory
        )

        for project, workers in assignments:
            #print(f"Projet assigné: {project.id}")
            self.apply_tags("before_cycle", project)

        if not self.consume_food():
            return False

        if self.season=="SAISON TEMPETE":
            if not self.consume_fuel():
                return False

        for project, workers in assignments:
            if workers < project.workers_required:
                continue

            if self.inventory.consume(project.inputs):
                if "RESSOURCE" in project.tags:
                    self.inventory.produce(project.outputs)
                for output in project.grants:
                    #print(f"construction de {output}")
                    self.requirements.add(output)

        return True

    def update_season(self, cycle):
        if cycle <= 2:
            self.season="BRUINE"
        elif cycle <= 5:
            self.season="ECLAIRCIE"
        else:
            self.season="TEMPETE"
        self.season = "SAISON " + self.season

    def run(self):

        for cycle in range(1, config.CYCLES + 1):
            if not self.cycle(cycle):
                return False

        return True