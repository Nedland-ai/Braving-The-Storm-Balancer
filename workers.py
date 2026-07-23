class Workers:

    def __init__(self, count):

        self.available = count

    def allocate(self, n):

        n = min(n, self.available)

        self.available -= n

        return n

    def reset(self, total):

        self.available = total