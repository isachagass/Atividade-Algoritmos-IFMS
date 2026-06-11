def calculo(numeros):
    numeros.sort()
    media = sum(numeros) / len(numeros)
    return print(f"Média = {media}\nMaior = {numeros[-1]}\nMenor = {numeros[0]}")
num = -1
numeros = []
while num != 0:
    num = int(input("Digite um número, ou 0 para sair: "))
    if num != 0:
        numeros.append(num)

calculo(numeros)