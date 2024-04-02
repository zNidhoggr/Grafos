import random
from .dangers import *
from .heal import *
from .weapons import *
from .creatures import *
from .island import *

class Region:
    def __init__(self, value: int, island):
        region_options = ["Praia", "Montanha", "Floresta", "Lago"]
        region_type = 0 if value == 0 else random.randint(1, len(region_options)-1)
        
        self.region_type = region_options[region_type]
        self.value = value
        self.paths = []
        self.events = []
        self.island = island
    
    def add_random_region_event(self):
        rand = 0
        events = [self.add_random_creature]
        events[rand]()
    
    def add_random_creature(self):
        existing_creatures = [c for c in self.events if isinstance(c, Creature)]
        if not existing_creatures:
            rand = random.randint(0, len(self.island.avaible_creatures) - 1)
            self.events.append(self.island.avaible_creatures[rand]())
        else:
            strongest_creature = max(existing_creatures, key=lambda c: c.attack_power)
            new_creature = random.choice([c for c in avaible_creatures if c != type(strongest_creature)])()
            self.handle_creature_encounter(strongest_creature, new_creature)
            for creature in existing_creatures:
                if creature != strongest_creature:
                    creature.health -= strongest_creature.attack_power
                    if creature.health <= 0:
                        self.events.remove(creature)
                    else:
                        print(f"O(A) {type(creature).__name__} fugiu da região {self.value}.")
                        self.events.remove(creature)
                        random_region = random.choice([r for r in isle.regions if r != self])
                        random_region.events.append(creature)
        
    def toString(self):     
        neighbors_str = ", ".join( (str(path.destination.value) for path in self.paths) ) #+ " Ao Longo De "+path.path_type)
       
        print(f"Vértice: {self.value}\n\tTipo: {self.region_type}\n\tVizinhos: {neighbors_str}")
           
        if self.event != None:
            print("\t", end="")
            self.event.use_attack()
        else: 
            print("\tSem evento nessa região")
        
        
 