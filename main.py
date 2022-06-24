from pokemon import *
from pessoa import *
from time import sleep
from pickle import dump, load  # biblioteca que transforma qualquer objeto em bytes


def escolher_pokemon_inicial(player):
    print("Olá {}, você poderá escolher agora o Pokemon que irá lhe acompanhar nessa jornada".format(player))

    pikachu = PokemonEletrico("Pikachu", level=1)
    charmander = PokemonFogo("Charmander", level=1)
    squirtle = PokemonAgua("Squirtle", level=1)

    print("Você possui três 3 escolhas:")
    print("1 - ", pikachu)
    print("2 - ", charmander)
    print("3 - ", squirtle)

    while True:
        escolha = input("Escolha o seu Pokemon: ")

        if escolha == "1":
            player.capturar(pikachu)
            break
        elif escolha == "2":
            player.capturar(charmander)
            break
        elif escolha == "3":
            player.capturar(squirtle)
            break
        else:
            print("Escolha inválida!")


def salvar_jogo(player):
    try:
        with open("database.db", "wb") as arquivo:
            dump(player, arquivo)  # joga o player dentro de arquivo, como bytes
            print("Jogo salvo com sucesso!!!")
    except Exception as error:
        print("Erro ao salvar o jogo: {}".format(error))


def carregar_jogo():
    try:
        with open("database.db", "rb") as arquivo:
            player = load(arquivo)
            print("Loading feito com sucesso!!!")
            return player
    except Exception as error:
        print("Save não encontrado.")


if __name__ == "__main__":
    print("-------------------------------------------------")
    print("    Bem-vindo ao game Pokemon RPG de terminal    ")
    print("-------------------------------------------------")

    player = carregar_jogo()

    if not player:      # Se não tiver player, vai para criar um, primeira batalha, etc.

        nome = input("Olá, qual é o seu nome: ")

        player = Player(nome)
        print("Olá {}, esse é um mundo habitado por Pokemons. Sua missão é se tornar um mestre dos pokemons.".format(player))
        print("Capture o máximo de pokemons que você conseguir e lute com seus amigos")
        player.mostrar_dinheiro()

        if player.pokemons:
            print("Já notei que você tem alguns pokemons")
            player.mostrar_pokemons()
        else:
            print("Você não tem nenhum pokemon. Escolha um")
            escolher_pokemon_inicial(player)

        print("Pronto, agora você poderá enfrentar seu arqui-rival desde o jardim da infância: Gary")
        gary = Inimigo(nome="Gary", pokemons=[PokemonAgua("Squirtle", level=1)])
        player.batalhar(gary)

        salvar_jogo(player)     # ao fim da primeira batalha, salva o jogo

    # Se já existir um player, vai para o menu principal
    while True:
        print("-----" * 10)
        print("O que você deseja fazer?")
        print('''1 - Explorar e tentar encontrar pokemons \n2 - Lutar com um inimigo \n3 - Ver pokemons \n4 - Ver saldo \n0 - Sair do jogo''')
        escolha = input("Escolha uma opção: ")

        if escolha == "0":
            print("Fechando o jogo...")
            sleep(1)
            break
        elif escolha == "1":
            player.explorar()
            salvar_jogo(player)
        elif escolha == "2":
            inimigo_aleatorio = Inimigo()
            player.batalhar(inimigo_aleatorio)
            salvar_jogo(player)
        elif escolha == "3":
            player.mostrar_pokemons()
        elif escolha == "4":
            player.mostrar_dinheiro()
        else:
            print("Opção inválida!!!")