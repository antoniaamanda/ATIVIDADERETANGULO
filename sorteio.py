import random 

numero_sorteado= random.randint(1,10)

for tentativa in range(1, 4):
    palpite= int(input(f"tentativa{tentativa}/3 - digite um número entre 1 e 10: "))

    if palpite == numero_sorteado:
        print("Parabéns! Você acertou o número sorteado!")
        break
    else:
        print("você errou.")

        if palpite < numero_sorteado:
            print("tente um número maior.")
        else:
            print("tente um número menor.")
        if tentativa == 3:
            print("você perdeu! fim de jogo")
            print(f"O número sorteado era:", numero_sorteado)