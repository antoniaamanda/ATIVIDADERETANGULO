senha_correta= 123456
tentativas = 3

nome= input("Digite seu nome:")

while tentativas > 0:
    senha = int(input("Digite sua senha: "))

    if senha == senha_correta:
        print(f"Olá, {nome}! Seja bem-vindo ao nosso banco.")
        break

    tentativas-=1

    if tentativas ==2:
        print("Senha incorreta! Você tem mais 2 tentativas.")
    elif tentativas ==1:
        print("Senha incorreta! Você tem mais 1 tentativa.")
    else:
        print("Sua senha foi bloqueada!Por favor dirija-se a um dos nossos caixas.")
    

