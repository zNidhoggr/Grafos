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

while True:
    print(f"Você está na região {explorer.current_region.value} ({explorer.current_region.region_type})")
    if explorer.has_treasure:
        print("Você já pegou o tesouro e pode sair da ilha.")
        break

    print("Escolha uma opção:")
    print("1. Mover para uma região vizinha")
    print("2. Usar item de cura")
    print("3. Abandonar arma")
    print("4. Sair do jogo")

    choice = input("> ")

    if choice == "1":
        print("Regiões vizinhas:")
        for i, path in enumerate(explorer.current_region.paths):
            print(f"{i + 1}. Região {path.destination.value} ({path.destination.region_type})")
        region_choice = int(input("Escolha uma região: "))
        if 1 <= region_choice <= len(explorer.current_region.paths):
            next_region = explorer.current_region.paths[region_choice - 1].destination
            explorer.move_to_region(next_region)
    elif choice == "2":
        # Implementar uso de itens de cura
        pass
    elif choice == "3":
        explorer.drop_weapon()
    elif choice == "4":
        break
    else:
        print("Opção inválida.")

isle.draw_graph()