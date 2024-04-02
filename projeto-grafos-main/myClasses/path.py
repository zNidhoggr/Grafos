import random
from .region import *

class Path: #Mesmo que aresta
    
    def __init__(self, region : Region):
        path_options = ["Uma Trilha Em Uma Floresta", "Um Paredão De Rochas", "Um Riacho"]
        self.destination = region
        self.path_type = path_options[random.randint(0, len(path_options)-1)]
        
