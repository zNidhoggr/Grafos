from abc import ABC, abstractmethod

class Heal(ABC):
    def __init__(self, healing_points):
        self.healing_points = healing_points
        
    @abstractmethod
    def use_heal():
        pass
    
class Plant(Heal):
    def use_heal():
        print("Cura com planta")
        
class Tree(Heal):
    def use_heal():
        print("Cura com arvore")