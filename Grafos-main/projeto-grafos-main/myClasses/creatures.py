from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self, health, attack):
        self.attack_power = attack
        self.health = health
    
    @abstractmethod
    def use_attack(self):
        pass

class Crocodile(Creature):
    def __init__(self):
        super().__init__(15, 5)
        
    def use_attack(self):
        print("Crocodilo atacando")
        
class Jaguar(Creature):
    def __init__(self):
        super().__init__(10, 15)
        
    def use_attack(self):
        print("Onça pintada atacando")
        
class Ant(Creature):
    def __init__(self):
        super().__init__(5, 10)
        
    def use_attack(self):
        print("Formigas quimera atacando")

avaible_creatures = [Crocodile, Jaguar, Ant]