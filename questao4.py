def fatorial(numero):
    resultado = 1

    for cont in range(numero, 0, -1):
        resultado *= cont

    return resultado


num = int(input("Digite um número: "))

while num != 0:
    print("Fatorial =", fatorial(num))

    num = int(input("Digite outro número (0 para parar): "))

print("Programa encerrado!")
