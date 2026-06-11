tipo= int(input("Qual é tipo do seu bilhete: \n1 - Unitário\n2 - Duplo\n3 - Viagens\n"))
valor = float(input("Quanto você vai dar: "))

unit = 1.3
duplo = 2.6
viagens = 12
quant = 0

if tipo == 1:
    while valor >= unit:
        valor -= unit
        quant += 1
elif tipo == 2:
    while valor >= unit:
        valor -= unit
        quant += 1

elif tipo == 3:
    while valor >= unit:
        valor -= unit
        quant += 1

print(f"Qunatidade de bilhetes: {quant}\nTroco: {valor:.2f}")