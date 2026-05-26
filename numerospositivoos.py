soma=0
cont=0 
maior=0
num=1
while num >0:
    num= int(input("Digite um número inteiro positivo: "))
    if num > 0:
        soma +=num
        cont+=1
    if num> maior:
        maior= num
print(f"a soma é:{soma}")
print(f"a média é:{soma/cont:.1f}")
print(f"o maior é:{maior}")