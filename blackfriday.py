opcao= -1

while opcao!= 0:
    print("\n=== BLACK FRIDAY ===")
    print("1 - TV")
    print("2- NOTEBOOK")
    print("3- CELULAR")
    print("0 - SAIR")

    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        print("TV em promoção por R$ 1999,90")
    elif opcao == 2:
        print("Notebook em promoção por R$ 3500,00")
    elif opcao == 3:
        print("Celular em promoção por R$ 1800,00")
    elif opcao == 0:
        print("Saindo do programa...")
    else:
        print("Opção inválida. Por favor, tente novamente.")
