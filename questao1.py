import radom

nomes= []

while true:
    nome= input("digite um nome :")

    if nome == "":
        break

    nomes.append(nome)
ganhador = random.choice(nomes)
print("o ganhador foi:", ganhador)