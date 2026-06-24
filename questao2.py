logins = []
senhas = []

usuario = input("crie um usuario:")
senha= input("crie uma senha:")


logins.append(usuario)
senhas.append(senha)

login = input("digite o usuario:")
senha_login = input("digite a senha:")

if login in logins:
    indice = logins.index(login)

    if senhas[indice] == senha_login:
        print("login realizado")
    else:
        print("senha incorreta")
else:
    print("usuario não cadrastado")