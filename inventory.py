class Inventory:

    def __init__(self, resources):
        self.resources = dict(resources)

    def has(self, costs):

        return all(
            self.resources.get(r, 0) >= amount
            for r, amount in costs.items()
        )

    def consume(self, costs):

        if not self.has(costs):
            return False

        for r, amount in costs.items():
            self.resources[r] -= amount

        return True

    def produce(self, outputs):

        for r, amount in outputs.items():
            self.resources[r] = self.resources.get(r, 0) + amount

    def copy(self):

        return Inventory(self.resources)