primeiro_termo= int(input("digite o primeiro termo:"))
quantidade= int(input("digite a quantidade de termos:"))
razao= int(input("digite a razão:"))

print("progressão aritmetica:")

for i in range(quantidade):
    termo= primeiro_termo + (i * razao)
    print(termo, end =" ")
