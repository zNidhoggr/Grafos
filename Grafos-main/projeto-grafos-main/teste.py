from myClasses.island import *
from myClasses.dangers import *
from myClasses.creatures import *
from myClasses.weapons import *
from myClasses.heal import *

helping_items = ["plantas e árvores medicinais", "Weapons"]

isle = Island()
isle.prepare_island(10)

explorer = Explorer("Aventureiro", isle)
explorer.current_region = isle.start_region

explorer.traverse_island()

isle.draw_graph()
