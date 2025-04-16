import random

while True:
    print("== DUELO DE HERÓIS ==")
    escolha = int(input("1 - Iniciar jogo\n"
                        "2 - Sair do jogo\n"
                        "Escolha a opção que deseja realizar: "))

    if escolha == 2:
        print("Jogo encerrado.")
        break
    else:
        jogador = input("Digite seu nick: ")
        inimigo = "inimigo"

        hp = random.randint(200, 1000)
        ataque1 = random.randint(1, 50)
        defesa1 = random.randint(1, 50)
        print(f"== {jogador} ==")
        print(f"HP: {hp}")
        print(f"ATQ: {ataque1}     DF: {defesa1}")

        ataque2 = random.randint(1, 50)
        defesa2 = random.randint(1, 50)
        print(f"== {inimigo} ==")
        print(f"HP: {hp}")
        print(f"ATQ: {ataque2}     DF: {defesa2}")

        hp_jog1 = hp
        hp_inim = hp

        while hp_jog1 or hp_inim > 0:

            print("== Turno 1 ==")
            print(f"HP de {jogador}: {hp_jog1} | HP de {inimigo}: {hp_inim}")
            acao = int(input(f"Vez de {jogador}. Escolha: [1] Atacar ou [2] Curar? "))
            print(f"{jogador} escolheu {acao}")
            if acao == 1:
                ataque = ataque1 - defesa2
                if ataque1 < defesa2:
                    ataque = 0
                print(f"O dano em {inimigo} foi de:", ataque)
                hp_inim -= ataque
            elif acao == 2:
                hp_jog1 += 10

            print("== Turno 2 ==")
            print(f"HP de {jogador}: {hp_jog1} | HP de {inimigo}: {hp_inim}")
            print(f"Vez de {inimigo}. Escolha: [1] Atacar ou [2] Curar?")
            acao = random.choices(["atacar", "curar"])
            print(f"{inimigo} escolheu {acao}")
            if acao == 1:
                ataque = ataque2 - defesa1
                if ataque2 < defesa1:
                    ataque = 0
                print(f"O dano em {jogador} foi de:", ataque)
                hp_jog1 -= ataque
            elif acao == 2:
                hp_inim += 10

            print(f"HP de {jogador}: {hp_jog1} | HP de {inimigo}: {hp_inim}")