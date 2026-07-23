def handle_immediate(project, settlement):
    # Execute immediately instead of at end of cycle
    pass


def handle_resource(project, settlement):
    # Resource projects may scale with workers
    pass


def handle_construction(project, settlement):
    # Add building to settlement
    pass


def handle_energy(project, settlement):
    # Increase energy pool
    pass


def handle_faction(project, settlement):
    # Verify faction requirements
    pass

def reveal_new_location(project, settlement):
    pass


TAG_HANDLERS = {
    "IMMEDIAT": {
        "before_cycle": handle_immediate,
    },
    "RESSOURCE": {
        "on_completion": handle_resource,
    },
    "CONSTRUCTION": {
        "on_completion": handle_construction,
    },
    "FACTION": {
        "before_assignment": handle_faction,
    },
    "EXPLORATION": {
        "on_completion": reveal_new_location,
    },
}