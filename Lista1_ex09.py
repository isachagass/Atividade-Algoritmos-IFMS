numeros = list(map(int, input("Digite 3 numeros separados por virgulas (,): ").split(',')))

soma = sum(numeros)
media = soma/3

print(f"Média = {media}")