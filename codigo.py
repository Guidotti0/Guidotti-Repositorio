import random

def criar_personagem(nome, oath):
    if oath == "Dawnwalker":
        vida = random.randint(100, 130)
        forca = random.randint(15, 20)
        magia = random.randint(5, 10)
    elif oath == "Blindseer":
        vida = random.randint(90, 110)
        forca = random.randint(10, 15)
        magia = random.randint(15, 25)
    else:
        vida = random.randint(80, 100)
        forca = random.randint(10, 15)
        magia = random.randint(10, 15)

    return {"nome": nome, "oath": oath, "vida": vida, "forca": forca, "magia": magia}

def lutar(jogador, inimigo):
    print(f"\n{jogador['nome']} ({jogador['oath']}) vs {inimigo['nome']} ({inimigo['oath']})")
    dano_jogador = jogador["forca"] + random.randint(0, 10)
    dano_inimigo = inimigo["forca"] + random.randint(0, 10)

    inimigo["vida"] -= dano_jogador
    jogador["vida"] -= dano_inimigo

    print(f"{jogador['nome']} causa {dano_jogador} de dano!")
    print(f"{inimigo['nome']} causa {dano_inimigo} de dano!")
    print(f"Vida restante - {jogador['nome']}: {jogador['vida']} | {inimigo['nome']}: {inimigo['vida']}")

def main():
    nome = input("Nome do personagem: ")
    print("Escolha seu Oath: Dawnwalker, Blindseer ou Nenhum")
    oath = input("Digite o oath: ")

    jogador = criar_personagem(nome, oath)
    inimigo = criar_personagem("Caçador das Sombras", random.choice(["Dawnwalker", "Blindseer", "Nenhum"]))

    print(f"\nPersonagem criado: {jogador['nome']} - Oath: {jogador['oath']}")
    print(f"Atributos: Vida={jogador['vida']}, Força={jogador['forca']}, Magia={jogador['magia']}")

    print(f"\nInimigo gerado: {inimigo['nome']} - Oath: {inimigo['oath']}")
    print(f"Atributos: Vida={inimigo['vida']}, Força={inimigo['forca']}, Magia={inimigo['magia']}")

    lutar(jogador, inimigo)

main()
