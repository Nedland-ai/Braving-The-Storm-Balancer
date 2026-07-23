from dataclasses import dataclass, field

@dataclass
class Project:

    id: str
    card: str
    name: str

    workers_required: int

    inputs: dict
    outputs: dict

    requirements: list = field(default_factory=list)
    grants: list = field(default_factory=list)
    tags: set = field(default_factory=set)

    def has_tag(self, tag: str):
        return tag in self.tags

    def is_available(self, settlement):
        for requirement in self.requirements:

            if requirement.startswith("BATIMENT "):
                if requirement not in settlement.requirements:
                    #print(f"Contrôle projet {self.id}: {requirement} manquant")
                    return False

            elif requirement.startswith("FACTION "):
                if requirement not in settlement.requirements:
                    #print(f"Contrôle projet {self.id}: {requirement} manquant")
                    return False

            elif requirement.startswith("SAISON "):
                if requirement != settlement.season:
                    #print(f"Contrôle projet {self.id}: {requirement} manquant")
                    return False

            else:
                print(f"Unknown requirement: {requirement}")

        #Do not rebuild a building already existing
        for requirement in self.grants:
            if requirement in settlement.requirements:
                return False
                
        return True    
