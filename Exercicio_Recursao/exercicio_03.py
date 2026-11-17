def contagem_regressiva(n):
    
    if n < 1:
        return

    print(n)
    contagem_regressiva(n-1)

print("Conatgem regressiva:")
contagem_regressiva(5)