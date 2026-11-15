def medias(lista, k):
    return sum(lista[0:k]) / k

lista = [0,1,2,3,4,5]
k= int(input("Digite o limite da janela: "))
resultado = medias(lista, k)
print(resultado)