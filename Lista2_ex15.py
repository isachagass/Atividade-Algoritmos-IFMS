numeros = list(map(int, input("Digite suas 3 notas: ").split(',')))
soma = sum(numeros)
media = soma/3
if media >= 0 and media < 3:
    print(f"Sua nota foi {media:.2f}, você está REPROVADO!")
elif media >= 3 and media <7:
    print(f"Sua nota foi {media:.2f}, EXAME!")
elif media >= 7 and media <= 10:
    print(f"Sua nota foi {media:.2f}, você está APROVADO!")