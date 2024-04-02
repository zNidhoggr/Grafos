import random
from math import ceil
from typing import List
from .region import *
from .path import *
from .dangers import *
from .creatures import *
from .heal import *
from .creatures import *
from .treasure import *
from .explorer import *
from .weapons import *
from .island import *

class Explorer:
    def __init__(self, name, island):
        self.name = name
        self.health = 100
        self.weapon = None
        self.healing_items = []
        self.current_region = island.start_region
        self.visited_regions = [island.start_region]
        self.has_treasure = False
        self.island = island
        
        
    def move_to_region(self, region):
        if region in self.visited_regions and region == self.island.start_region:
            if region in self.visited_regions and not self.has_treasure:
                print("Você não pode voltar a essa região antes de pegar o tesouro!")
                return
            elif region in self.visited_regions and self.has_treasure:
                return -1


        self.current_region = region
        self.visited_regions.append(region)

        if region == self.island.treasure_region:
            self.get_treasure()
        else:
            self.handle_region_events(region)

    def drop_weapon(self, weapon):
        if(weapon == None):
            print("Voce nao tem arma")
        else:
            weapon = None
    def get_treasure(self):
        treasure = next((event for event in self.current_region.events if isinstance(event, Treasure)), None)
        if treasure:
            treasure_value = treasure.value
            if self.weapon:
                treasure_value += self.weapon.damage
            treasure_value += self.health
            self.has_treasure = True
            print(f"Você pegou o tesouro de valor {treasure_value}!")
        else:
            print("Não há tesouro nessa região.")

    def handle_region_events(self, region):
        # Lidar com eventos na região

        pass
    def battle(self, creature):
        print(f"Você encontrou um(a) {type(creature).__name__} na região {self.current_region.value}!")
        
        turns = 3  # Número de turnos da batalha
        
        while turns > 0:
            # Turno do jogador
            print("1. Atacar")
            print("2. Fugir")
            choice = input("> ")
            
            if choice == "1":
                if self.weapon:
                    creature.health -= self.weapon.damage
                    print(f"Você atacou o(a) {type(creature).__name__} com sua {type(self.weapon).__name__} e causou {self.weapon.damage} de dano.")
                else:
                    print("Você não está portando nenhuma arma.")
            elif choice == "2":
                print("Você fugiu da batalha.")
                return
            
            # Turno da criatura
            if creature.health > 0:
                self.health -= creature.attack_power
                print(f"O(A) {type(creature).__name__} atacou você e causou {creature.attack_power} de dano.")
            
            turns -= 1
        
        # Verificar resultado da batalha
        if self.health <= 0:
            print("Você foi derrotado!")
        elif creature.health <= 0:
            print(f"Você derrotou o(a) {type(creature).__name__}!")
            self.current_region.events.remove(creature)
        else:
            print("A batalha terminou em empate!")
            print("1. Lutar novamente")
            print("2. Fugir")
            choice = input("> ")
            if choice == "1":
                self.battle(creature)
            else:
                print("Você fugiu da batalha.")