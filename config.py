SIMULATIONS = 1000

CYCLES = 8

FOOD_CYCLES = range(1, 9)
FUEL_CYCLES = range(6, 9)

SURVIVAL_WEIGHTS = {
    "NOURRITURE": 1,
    "BOIS": 1,
    "RESSOURCE": 1,
    "CONSTRUCTION": 1,
}

ALLOCATOR = "weighted_random"
RANDOM_SEED = None

# Amount of randomness added to each project's score
RANDOMNESS = 1.0

# Score multiplier for each duplicate instance
DUPLICATE_DECAY = 0.7

NON_REPEATABLE_TAGS = {
    "CONSTRUCTION",
    "UNIQUE",
}

PROJECTS_FILE_PATH="data/projects.xlsx"