def editar_cliente(cod_cli):

    arq_clientes = open(
        file='clientes.txt',
        mode='r',
        buffering=-1,
        encoding='utf-8',
        errors='replace'
    )

    encontrado = False
    titulos = arq_clientes.readline()
    dados = []

    if titulos:
        dados.append(titulos)

    for linha in arq_clientes:
        cliente = linha.strip().split(';')
        

        if len(cliente) > 0:
            if cliente[0] == cod_cli:
                encontrado = True

                nome = input("Digite o nome: ")
                endereco = input("Digite o endereço: ")
                fone = input("Digite o numero de telefone: ")
                
                novo = f'{cod_cli};{nome};{endereco};{fone}\n'
                dados.append(novo)
            else:
                dados.append(linha)

    arq_clientes.close()

    if not encontrado:
        print("Cliente não encontrado")
        return 
    else:
        arq_clientes = open(
            file='clientes.txt',
            mode='w',
            buffering=-1,
            encoding='utf-8',
            errors='replace'
        )

        arq_clientes.writelines(dados)
        arq_clientes.close()

        print("Cliente alterado!")
        
    


cod_cli = input("Digite o codigo do cliente para editar: ")
editar_cliente(cod_cli)



