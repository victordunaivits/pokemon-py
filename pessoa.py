from pokemon import *
from random import choice, randint, random

NOMES = [
    "isaias", "Isabela", "Marcos", "joselito", "Raimundão", "Carlos", "Red", "Blue"
]

POKEMONS = [
    PokemonFogo("charmander"),
    PokemonFogo("Flarion"),
    PokemonFogo("Charmilion"),
    PokemonEletrico("Pikachu"),
    PokemonEletrico("Raichu"),
    PokemonAgua("Squirtle"),
    PokemonAgua("Magicarp")
]


class Pessoa:
    def __init__(self, nome=None, pokemons=[], dinheiro=100):
        if nome:
            self.nome = nome
        else:
            self.nome = choice(NOMES)

        self.pokemons = pokemons

        self.dinheiro = dinheiro

    def __str__(self):
        return self.nome

    def mostrar_pokemons(self):
        if self.pokemons:
            print("Pokemons de {}:".format(self))
            for index, pokemon in enumerate(self.pokemons):
                print("{} - {}".format(index, pokemon))
        else:
            print("{} não tem pokemons!".format(self))

    def escolher_pokemon(self):
        if self.pokemons:
            pokemon_escolhido = choice(self.pokemons)
            print("{} escolheu {}".format(self, pokemon_escolhido))
            return pokemon_escolhido
        else:
            print("ERRO: jogador sem pokemons!")

    def mostrar_dinheiro(self):
        print("Você possui R$ {} em sua conta.".format(self.dinheiro))

    def ganhar_dinheiro(self, quantidade):
        self.dinheiro += quantidade
        print("Você ganhou R$ {}".format(quantidade))
        self.mostrar_dinheiro()

    def batalhar(self, pessoa):
        print("{} iniciou uma batalha com {}".format(self, pessoa))

        pessoa.mostrar_pokemons()
        pokemon_inimigo = pessoa.escolher_pokemon()

        pokemon = self.escolher_pokemon()

        if pokemon and pokemon_inimigo:
            while True:
                if pokemon.atacar(pokemon_inimigo):  # Caso retorne True, seu pokemon vence a batalha
                    print("{} ganhou a batalha".format(self))
                    self.ganhar_dinheiro(pokemon_inimigo.level * 100)   # caso vença, ganha dinheiro baseado no level do inimigo
                    break
                if pokemon_inimigo.atacar(pokemon):  # Caso retorne True, pokemon inimigo vence
                    print("{} ganhou a batalha".format(pessoa))
                    break
        else:
            print("Essa batalha não pode ocorrer!!!")


# Classes que herdaram as caracteristicas da classe Pessoa
class Player(Pessoa):
    tipo = "player"

    def capturar(self, pokemon):
        self.pokemons.append(pokemon)
        print("{} capturou {}!".format(self, pokemon))

    def escolher_pokemon(self):
        self.mostrar_pokemons()

        if self.pokemons:
            while True:
                escolha = input("Escolha seu pokemon: ")
                try:
                    escolha = int(escolha)
                    pokemon_escolhido = self.pokemons[escolha]
                    print("{} eu escolho você!!!".format(pokemon_escolhido))
                    return pokemon_escolhido
                except:
                    print("Escolha inválida!")
        else:
            print("Esse jogador não possue pokemons")

    # método para explorar oara encontrar um pokemon. biblioteca random para trabalhar com probabilidade de 30% de encontrar pokemon
    def explorar(self):
        if random() <= 0.3:
            pokemon = choice(POKEMONS)
            print("Um pokemon selvagem apareceu no radar: {}".format(pokemon))

            op = input("Deseja capturar esse pokemon? (s/n): ")
            if op == "s" or op == "S":
                if random() >= 0.5:     # fazemos um random simples para que haja 50% de chance de conseguir capturar o pokemon
                    self.capturar(pokemon)
                else:   # Caso contrário, pokemon foge!
                    print("Pokemon {} escapou!".format(pokemon))
            elif op == "n" or op == "N":
                print("Até logo!")
            else:
                print("Opção inválida!")
        else:
            print("Exploração terminada. Sem pokemons!")


class Inimigo(Pessoa):
    tipo = "inimigo"

    def __init__(self, nome=None, pokemons=None):
        if not pokemons:
            pokemons_aleatorios = []
            for i in range(randint(1, 6)):  # escolhe pokemons aleatório para o inimigo
                pokemons_aleatorios.append(choice(POKEMONS))
            
            super(Inimigo, self).__init__(nome=nome, pokemons=pokemons_aleatorios)
        else:
            super().__init__(nome=nome, pokemons=pokemons)