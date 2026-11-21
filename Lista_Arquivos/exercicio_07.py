def criar():
    produtos = open(
        file='produtos.csv',
        mode='w',
        buffering=-1,
        encoding='utf-8',
        errors='replace'
    )
    produtos.write("codigo;descricao;preco\n")
    produtos.close()

    print("\nArquivo criado!\n")
    return


def post():
    
    numero = int(input("Digite o codigo do produto: "))

    produtos = open(
        file='produtos.csv',
        mode='r',
        buffering=-1,
        encoding='utf-8',
        errors='replace'
    )

    produtos.readline()
    existe = False

    for linha in produtos:
        dado = linha.strip().split(";")

        if dado[0] == numero:
            existe = True
            break

    produtos.close()

    if existe:
        print("Este codigo já existe!")
    else:
        descricao = input("Digite a descricao do produto: ")
        preco = float(input("Digite o preco do produto: "))

        produtos = open(
            file='produtos.csv',
            mode='a',
            buffering=-1,
            encoding='utf-8',
            errors='replace'
        )
        

        dados = f'{numero};{descricao};{preco}\n'
        produtos.write(dados)
        print("Produto cadastrado!")

        produtos.close()

    return


def get():
    
    produtos = open(
        file='produtos.csv',
        mode='r',
        buffering=-1,
        encoding='utf-8',
        errors='replace'
    )

    produtos.readline()
    print("\nProdutos cadastrados: \n")

    for linha in produtos:
        dado = linha.strip().split(';')

        if len(dado) >= 3:
            print(f"Numero: {dado[0]} | Descricao: {dado[1]} | Preco: R${dado[2]}")

    produtos.close()
      

def update():
    numero = input("Digite o numero do produto para alterar: ")

    produtos = open(
        file='produtos.csv',
        mode='r',
        buffering=-1,
        encoding='utf-8',
        errors='replace'
    )

    encontrado = False
    titulos = produtos.readline()
    dados = []

    if titulos:
        dados.append(titulos)

    for linha in produtos:
        prod = linha.strip().split(';')
        

        if len(prod) > 0:
            if prod[0] == numero:
                encontrado = True

                descricao = input("Digite a nova descricao: ")
                preco = float(input("Digite o novo preco: "))
                
                novo = f'{numero};{descricao};{preco}\n'
                dados.append(novo)
            else:
                dados.append(linha)

    produtos.close()

    if not encontrado:
        print("\nProduto não encontrado")
        return 
    else:
        produtos = open(
            file='produtos.csv',
            mode='w',
            buffering=-1,
            encoding='utf-8',
            errors='replace'
        )

        produtos.writelines(dados)
        produtos.close()

        print("Produto alterado!")


def delete():
    numero = input("Digite o numero do produto para deletar: ")

    produtos = open(
        file='produtos.csv',
        mode='r',
        buffering=-1,
        encoding='utf-8',
        errors='replace'
    )

    titulo = produtos.readline()
    dados = []
    encontrou = False

    if titulo:
        dados.append(titulo)

    for linha in produtos:
        prod = linha.strip().split(";")
        if len(prod) > 0:
            if prod[0] == numero:
                encontrou = True
            else: 
                dados.append(linha)

    produtos.close()

    if not encontrou:
        print("O produto não foi encontrado!")
    else:
        produtos = open(
            file='produtos.csv',
            mode='w',
            buffering=-1,
            encoding='utf-8',
            errors='replace'
        )

        produtos.writelines(dados)
        produtos.close()
        print("\nProduto deletado!")


while True:
    opcao = int(input("\nEscolha uma opção:\n1. Criar Arquivo\n2. POST\n3. GET\n4. UPDATE\n5. DELETE\n6. SAIR\n"))

    if opcao == 1:
        criar()
    elif opcao == 2:
        post()
    elif opcao == 3:
        get()
    elif opcao == 4:
        update()
    elif opcao == 5:
        delete()
    elif opcao == 6: 
        break
    else:
        print("Digite uma opção válida!")
