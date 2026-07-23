from dataclasses import dataclass
import random
import config


@dataclass
class Candidate:
    project: object
    iteration: int
    score: float
    assigned_workers: int


def score(project):

    value = random.uniform(0, config.RANDOMNESS)

    for tag in project.tags:
        value += config.SURVIVAL_WEIGHTS.get(tag, 0)

    for resource, amount in project.outputs.items():
        value += config.SURVIVAL_WEIGHTS.get(resource, 0) * amount

    return value



def max_runs(project, workers, inventory):
    """
    Maximum number of times this project could theoretically be run.
    """

    if any(tag in config.NON_REPEATABLE_TAGS for tag in project.tags):
        return 1

    # Free projects should only appear once
    if project.workers_required == 0 and not project.inputs:
        return 1

    if project.workers_required == 0:
        worker_limit = 999999
    else:
        worker_limit = workers.available // project.workers_required

    resource_limit = worker_limit

    for resource, amount in project.inputs.items():

        if amount <= 0:
            continue

        available = inventory.resources.get(resource, 0)

        resource_limit = min(resource_limit, available // amount)

    return max(0, min(worker_limit, resource_limit))


def generate_candidates(projects, workers, inventory):
    candidates = []

    for project in projects:
        runs = max_runs(project, workers, inventory)
        base = score(project)

        for i in range(runs):
            candidates.append(
                Candidate(
                    project=project,
                    iteration=i,
                    score=base * (config.DUPLICATE_DECAY ** i),
                    assigned_workers=project.workers_required
                )
            )

    return candidates


def allocate(projects, workers, inventory):
    """
    Returns:
        [(project, assigned_workers), ...]
    """

    planning_inventory = inventory.copy()
    available_workers = workers.available
    candidates = generate_candidates(
        projects,
        workers,
        planning_inventory
    )
    candidates.sort(
        key=lambda c: c.score,
        reverse=True
    )
    assignments = []

    for candidate in candidates:
        #(f"Projet {candidate.project.id} {candidate.iteration}, Score {candidate.score}")
        project = candidate.project

        # enough workers?
        if available_workers < project.workers_required:
            continue

        # enough resources?
        if not planning_inventory.has(project.inputs):
            continue

        # reserve workers
        available_workers -= project.workers_required

        # reserve resources
        planning_inventory.consume(project.inputs)

        assignments.append(
            (
                project,
                project.workers_required
            )
        )

    return assignments