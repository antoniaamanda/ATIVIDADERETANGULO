def ordenar(lista):
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] > lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
    return lista

lista = [int(x) for x in input("Digite os números separados por espaço: ").split()]

print(ordenar(lista))
