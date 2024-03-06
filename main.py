import random

# Classe para representar o personagem
class Personagem:
    def __init__(self):
        self.pontos_de_vida = 100
        self.pontos_de_ataque = 10
        self.arma = None
        self.tesouro = 0
        self.checkpoints = []

    def pegar_arma(self, arma):
        if self.arma:
            print("Você já está carregando uma arma.")
        else:
            self.arma = arma
            self.pontos_de_ataque += arma.pontos_de_ataque
            self.tesouro = max(0, self.tesouro - arma.pontos_de_ataque)
            print(f"Você pegou a {arma.nome} (+{arma.pontos_de_ataque} pontos de ataque)")

    def abandonar_arma(self):
        if self.arma:
            self.pontos_de_ataque -= self.arma.pontos_de_ataque
            arma = self.arma
            self.arma = None
            print(f"Você abandonou a {arma.nome}")
        else:
            print("Você não está carregando nenhuma arma.")

    def batalhar(self, criatura):
        print(f"Você encontrou um(a) {criatura.nome}")
        escolha = input("Deseja batalhar ou fugir? (b/f) ")

        if escolha.lower() == "f":
            self.pontos_de_vida -= criatura.pontos_de_ataque
            print(f"Você fugiu e perdeu {criatura.pontos_de_ataque} pontos de vida.")
            return

        for turno in range(3):
            if turno % 2 == 0:
                dano = random.randint(1, self.pontos_de_ataque)
                criatura.pontos_de_vida -= dano
                print(f"Você atacou o(a) {criatura.nome} e causou {dano} pontos de dano.")
            else:
                dano = random.randint(1, criatura.pontos_de_ataque)
                self.pontos_de_vida -= dano
                print(f"O(A) {criatura.nome} atacou você e causou {dano} pontos de dano.")

            if criatura.pontos_de_vida <= 0:
                print(f"Você derrotou o(a) {criatura.nome}!")
                self.tesouro = int(self.pontos_de_vida * self.tesouro / 100)
                return
            elif self.pontos_de_vida <= 0:
                print("Você foi derrotado!")
                return

        print("A batalha terminou em empate!")

    def restaurar_vida(self, pontos):
        self.pontos_de_vida = min(100, self.pontos_de_vida + pontos)
        print(f"Você recuperou {pontos} pontos de vida.")

    def encontrar_checkpoint(self):
        self.checkpoints.append((self.pontos_de_vida, self.pontos_de_ataque, self.arma))
        print("Você encontrou um checkpoint!")

    def morrer(self):
        if not self.checkpoints:
            print("Você morreu e não há mais checkpoints. Game Over!")
            return True

        self.pontos_de_vida, self.pontos_de_ataque, self.arma = self.checkpoints.pop()
        self.tesouro = int(self.pontos_de_vida * self.tesouro / 100)
        print("Você foi revivido no último checkpoint encontrado.")
        return False

# Classe para representar criaturas
class Criatura:
    def __init__(self, nome, pontos_de_vida, pontos_de_ataque):
        self.nome = nome
        self.pontos_de_vida = pontos_de_vida
        self.pontos_de_ataque = pontos_de_ataque

# Classe para representar armas
class Arma:
    def __init__(self, nome, pontos_de_ataque, usos_restantes):
        self.nome = nome
        self.pontos_de_ataque = pontos_de_ataque
        self.usos_restantes = usos_restantes

# Função para criar o grafo da ilha
def criar_grafo(num_vertices):
    grafo = {}
    for i in range(num_vertices):
        grafo[i] = []

    # Adicionar arestas aleatórias
    for i in range(num_vertices):
        for j in range(i + 1, num_vertices):
            if random.random() < 0.3:
                grafo[i].append(j)
                grafo[j].append(i)

    return grafo

# Função para adicionar elementos à ilha
def adicionar_elementos(grafo, num_criaturas, num_armas, num_perigos, num_checkpoints):
    criaturas = [
        Criatura("Crocodilo Gigante", 80, 25),
        Criatura("Onça Pintada", 60, 30),
        Criatura("Formigas Quimera", 40, 20)
    ]
    armas = [
        Arma("Espada Antiga", 15, 3),
        Arma("Arco e Flechas", 10, 3),
        Arma("Lança Afiada", 12, 3)
    ]
    perigos = ["Gás Venenoso", "Poço de Piche", "Areia Movediça", "Planta Venenosa"]

    for vertice in grafo:
        grafo[vertice] = []
        if random.random() < num_criaturas / num_vertices:
            grafo[vertice].append(random.choice(criaturas))
        if random.random() < num_armas / num_vertices:
            grafo[vertice].append(random.choice(armas))
        if random.random() < num_perigos / num_vertices:
            grafo[vertice].append(random.choice(perigos))
        if num_checkpoints > 0:
            if random.random() < 1 / num_vertices:
                grafo[vertice].append("Checkpoint")
                num_checkpoints -= 1

# Função para explorar a ilha
def explorar_ilha(grafo, personagem, vertice_inicial, vertice_final):
    fila = [(vertice_inicial, 0)]
    visitados = set()
    while fila:
        vertice_atual, tempo = fila.pop(0)
        if tempo > 3 * len(grafo):
            print("Você ficou preso na ilha!")
            return 0

        if vertice_atual == vertice_final:
            print(f"Você encontrou {personagem.tesouro}% do tesouro!")
            return personagem.tesouro

        if vertice_atual in visitados:
            continue

        visitados.add(vertice_atual)
        print(f"Você está no vértice {vertice_atual}")

        elementos = grafo[vertice_atual]
        for elemento in elementos:
            if isinstance(elemento, Criatura):
                personagem.batalhar(elemento)
                if personagem.pontos_de_vida <= 0:
                    if personagem.morrer():
                        return 0
            elif isinstance(elemento, Arma):
                escolha = input(f"Você encontrou a {elemento.nome} (+{elemento.pontos_de_ataque} pontos de ataque, {elemento.usos_restantes} usos restantes). Deseja pegá-la? (s/n) ")
                if escolha.lower() == "s":
                    personagem.pegar_arma(elemento)
            elif elemento == "Checkpoint":
                personagem.encontrar_checkpoint()
            else:
                print(f"Você encontrou um {elemento}!")
                personagem.pontos_de_vida -= 10
                if personagem.pontos_de_vida <= 0:
                    if personagem.morrer():
                        return 0

        for vizinho in grafo[vertice_atual]:
            fila.append((vizinho, tempo + 1))

    print("Você não encontrou o tesouro a tempo!")
    return 0

# Exemplo de uso
num_vertices = 20
grafo = criar_grafo(num_vertices)
adicionar_elementos(grafo, num_criaturas=4, num_armas=3, num_perigos=3, num_checkpoints=3)

personagem = Personagem()
vertice_inicial = 0
vertice_final = num_vertices - 1

tesouro_encontrado = explorar_ilha(grafo, personagem, vertice_inicial, vertice_final)
