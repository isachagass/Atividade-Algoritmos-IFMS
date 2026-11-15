def deslocar(lista, n):
    for i in range(n):
        lista.insert(0, lista[-1])
        lista.pop()
    return lista

lista = [1,2,3,4,5]
n = int(input("Digite o numero de casas que serão deslocadas: "))
print(deslocar(lista, n))