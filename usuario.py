a= int(input("digite o valor de a: "))
b= int(input("didite o valor de b: "))

if a < b:
    soma=0

    for i in range(a,b + 1):
        soma += i

        print("A soma dos números no intervalo é: ",soma) 
else: 
    print("Erro: o valor de a deve ser menor que o valor de b.")  
