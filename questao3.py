usuarios = {}

usuario = input("crie um usuario:")
senha = input("crie uma senha:")

usuarios[usuario] = senha

login= input("digite o usuario:")
senha_login = input("digite a senha:")

if login in usuarios and usuarios[login]== senha_login:
    print("login realizado")
else:
    print("usuario ou senha incorretos")