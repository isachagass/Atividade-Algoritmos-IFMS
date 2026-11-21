def criar():
    registros = open(
        file='registros.txt',
        mode='w',
        buffering=-1,
        encoding='utf-8',
        errors='replace'
    )
    registros.write("numero;nome;nota1;nota\n")
    registros.close()

    print("\nArquivo criado!\n")
    return


def incluir():
    registros = open(
        file='registros.txt',
        mode='a',
        buffering=-1,
        encoding='utf-8',
        errors='replace'
    )

    while True:
        numero = int(input("Digite o numero do registro - ou 0 para encerrar: "))

        if numero == 0:
            break

        nome = input("Digite o nome do registro: ")
        nota1 = float(input("Digite a nota 1 do registro: "))
        nota2 = float(input("Digite a nota 2 do registro: "))

        dados = f'{numero};{nome};{nota1};{nota2}\n'
        registros.write(dados)
        print("Registro criado!")

    registros.close()

    registros = open(
        file='registros.txt',
        mode='r',
        buffering=-1,
        encoding='utf-8',
        errors='replace'
    )

    registros.readline()
    print("\nDados cadastrados: \n")

    for linha in registros:
        dado = linha.strip().split(';')

        if len(dado) >= 4:
            print(f"Numero: {dado[0]} | Nome: {dado[1]} | Nota1: {dado[2]} | Nota2: {dado[3]} | Media: {(float(dado[2])+float(dado[3]) )/ 2}")
      

    return

while True:
    opcao = int(input("\nEscolha uma opção:\n1. Criar\n2. Incluir\n3. Sair\n"))

    if opcao == 1:
        criar()
    elif opcao == 2:
        incluir()
    elif opcao == 3:
        break
    else:
        print("Digite uma opção válida!")
