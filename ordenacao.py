def quick_sort(valores):
    # Caso base: se a lista tiver 0 ou 1 item, ela ja esta organizada.
    # Usamos o retorno antecipado para evitar o uso de else ou elif.
    if len(valores) <= 1:
        return valores

    # Escolha do pivo: pegamos o elemento que esta bem no meio da lista.
    indice_pivo = len(valores) // 2
    pivo = valores[indice_pivo]

    # Criamos as listas vazias para separar os elementos em relacao ao pivo.
    menores = []
    iguais = []
    maiores = []

    # Comparamos cada item e distribuimos nas listas correspondentes.
    for item in valores:
        if item < pivo:
            menores.append(item)
        if item == pivo:
            iguais.append(item)
        if item > pivo:
            maiores.append(item)

    # Chamada recursiva para ordenar as sublistas e juntar o resultado final.
    return quick_sort(menores) + iguais + quick_sort(maiores)
# Mude de: print(quick_sort())
# Para exatamente isto:
print(quick_sort([7, 3, 9, 1, 5]))
