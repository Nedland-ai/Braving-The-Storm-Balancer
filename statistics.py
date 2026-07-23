from collections import defaultdict

class Statistics:

    def __init__(self):

        self.successes = 0
        self.total = 0

        self.resources = defaultdict(list)
        self.requirements = defaultdict(list)

    #Enregistrer le résultat du run.
    def record(self, success, inventory, requirements):

        self.total += 1

        if success:
            self.successes += 1

        for r, amount in inventory.resources.items():
            self.resources[r].append(amount)

        for requirement in requirements:
            self.requirements[requirement].append(1)

    @property
    def success_rate(self):

        return 100 * self.successes / self.total