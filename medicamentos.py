mais_barato=""
menor_preco= 0
soma = 0

for i in range(5):
    nome = input(f"Digite o nome do medicamento {i+1}: ")
    preco= float(input("Digite o preço do medicamento: R$"))

    soma+= preco

    if i ==0 or preco < menor_preco:
        menor_preco = preco
        mais_barato = nome

media = soma / 5

print("\n === RESULTADOS ===")
print(f"Medicamento mais barato: {mais_barato}")
print(f"Menor preço: R$ {menor_preco:.2f}")
print(f"Média dos preços: R$ {media:.2f}")
