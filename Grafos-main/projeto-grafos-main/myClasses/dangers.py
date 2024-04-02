from abc import ABC, abstractmethod


class Danger(ABC):
    def __init__(self, damage) -> None:
        self.damage = damage
    
    @abstractmethod
    def toString(self):
        pass

class Passage(Danger):
    def toString(self):
        print("passagem escorregadia à beira de um abismo")
        
class DangerousAnimal(Danger):
    def toString(self):
        print("animal selvagem perigoso")
        
class PoisonousAnimal(Danger):
    def toString(self):
        print("animal selvagem venenoso")
        
class Quicksand(Danger):
    def toString(self):
        print("poço de areia movediça e de piche")
        
class PoisonousPlant(Danger):
    def toString(self):
        print("planta venenosa com frutos chamativo e aparentemente suculento")


avaible_dangers = [Passage, DangerousAnimal, PoisonousAnimal, Quicksand, PoisonousPlant]