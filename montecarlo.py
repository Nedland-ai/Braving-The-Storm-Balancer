from settlement import Settlement
from statistics import Statistics

def run(simulations,
        resources,
        workers,
        projects):

    stats = Statistics()

    for _ in range(simulations):

        s = Settlement(
            resources,
            workers,
            projects
        )

        success = s.run()

        stats.record(
            success,
            s.inventory,
            s.requirements
        )

    return stats