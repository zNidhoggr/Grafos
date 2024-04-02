from abc import ABC, abstractmethod


class Weapon(ABC):
    def __init__(self, damage):
        self.damage = damage

    @abstractmethod
    def toString():
        pass 
    
class FireStaff(Weapon):
    def toString(self):
        print("Atacando com Cajado de Fogo")

class Sword(Weapon):
    def toString(self):
        print("Atacando com Espada")

class Bow(Weapon):
    def toString(self):
        print("Atacando com Arco")

class Shuriken(Weapon):
    def toString(self):
        print("Atacando com Shuriken")


avaible_weapons = [FireStaff, Sword, Bow, Shuriken]