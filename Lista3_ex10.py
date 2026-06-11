primos = []
for i in range(2,20000):
    raiz = i ** 0.5
    primo = True
    for j in range(2,int(raiz)+1):
        if i % j == 0:
            primo = False
            break
    if primo:
        primos.append(i)

print(primos)