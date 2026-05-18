opcao= -1

while opcao !=0:

    print("\n*** Calculadora de Números reais***")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("0. Sair")

    opcao = int(input("Escolha a operação desejada:"))

    if opcao==0:
        print("Programa encerrado.")
    elif opcao>=1 and opcao<=4:
        num1 = float(input("Digite o número 1:"))
        num2 = float(input("Digite o número 2:"))
        if opcao==1:
            resultado = num1 + num2
            print(" O resultado é: %.2f" % resultado)

        elif opcao==2:
            resultado= num1-num2
            print(" O resultado é: %.2f" % resultado)
        elif opcao==3:
            resultado= num1*num2
            print(" O resultado é: %.2f" % resultado)
        elif opcao==4:
            if num2 !=0:
                resultado= num1/num2
                print(" O resultado é: %.2f" % resultado)
            else:
                print("Não é possível dividir por zero.")

    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
