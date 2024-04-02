from .region import *
from .path import *
from .dangers import *
from .creatures import *
from .heal import *
from .creatures import *
from .treasure import *
from .explorer import *
from .weapons import *
from math import ceil
import random
from math import ceil
from typing import List

class Island:
    def __init__(self):
        self.regions = []
        self.start_region = None
        self.treasure_region = None

    def add_region(self, value: int) -> Region:
        new_region = Region(value, self)
        self.regions.append(new_region)
        if value == 0:
            self.start_region = new_region
        return new_region

    def add_path(self, region1: Region, region2: Region):
        region1.paths.append(Path(region2))
        region2.paths.append(Path(region1))

    def toString(self):
        for region in self.regions:
            region.toString()
            print("")

    def prepare_island(self, num_regions: int):
        self.number_of_regions = num_regions

        # Cria quantidade de regiões passadas por parâmetro
        for index in range(0, num_regions):
            new_region = self.add_region(index)

            # Cria aresta entre a nova região criada e todas criadas anteriormente
            for region in self.regions[:-4]:
                self.add_path(new_region, region)

        # Adicionar tesouro em uma região aleatória, exceto a inicial
        treasure_region_index = random.randint(1, num_regions - 1)
        self.treasure_region = self.regions[treasure_region_index]
        treasure_value = random.randint(50, 100)  # Valor do tesouro entre 50 e 100
        self.treasure_region.events.append(Treasure(treasure_value))

        num_events = int(ceil(num_regions * 0.3))
        print(f"Número de eventos: {num_events}")

        available_regions = self.regions[:]
        available_creatures = avaible_creatures[:]
        available_dangers = avaible_dangers[:]
        available_weapons = avaible_weapons[:]

        while num_events > 0:
            region_index = random.randint(0, len(available_regions) - 1)
            region = available_regions.pop(region_index)

            event_type = random.randint(1, 3)  # 1: Criatura, 2: Perigo, 3: Arma
            if event_type == 1 and available_creatures:
                creature_index = random.randint(0, len(available_creatures) - 1)
                creature = available_creatures.pop(creature_index)
                region.events.append(creature())
                num_events -= 1
            elif event_type == 2 and available_dangers:
                danger_index = random.randint(0, len(available_dangers) - 1)
                danger = available_dangers.pop(danger_index)
                region.events.append(danger(random.randint(5, 15)))
                num_events -= 1
            elif event_type == 3 and available_weapons:
                weapon_index = random.randint(0, len(available_weapons) - 1)
                weapon = available_weapons.pop(weapon_index)
                region.events.append(weapon(random.randint(5, 15)))
                num_events -= 1

    def draw_graph(self):
        import networkx as nx
        import matplotlib.pyplot as plt

        G = nx.Graph()

        # Adicionar vértices
        for region in self.regions:
            G.add_node(region.value, label=region.region_type)

        # Adicionar arestas
        for region in self.regions:
            for path in region.paths:
                G.add_edge(region.value, path.destination.value)

        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True)
        plt.show()