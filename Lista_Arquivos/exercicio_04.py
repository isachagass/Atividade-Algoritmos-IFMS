def excluir_cliente(cod_cli):
    excluido = False

    arq_clientes = open(
        file='clientes.txt',
        mode='r',
        buffering=-1,
        encoding='utf-8',
        errors='replace'
    )

    titulos = arq_clientes.readline()
    dados = []

    if titulos:
        dados.append(titulos)

    for linha in arq_clientes:
        cliente = linha.strip().split(';')
        

        if len(cliente) > 0:
            if cliente[0] == cod_cli:
                excluido = True
            else:
                dados.append(cliente)

    arq_clientes.close()

    if not excluido:
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
        excluir_recibo(cod_cli)
    

def excluir_recibo(cod_cli):
    arq_recibo = open(
        file='recebimentos.txt',
        mode='r',
        buffering=-1,
        encoding='utf-8',
        errors='replace'
    )

    titulo = arq_recibo.readline()
    dados = []
    encontrou = False

    if titulo:
        dados.append(titulo)

    for linha in arq_recibo:
        recibo = linha.strip().split(";")
        if len(recibo) > 0:
            if recibo[4] == cod_cli:
                encontrou = True
            else: 
                dados.append(recibo)

    arq_recibo.close()

    if not encontrou:
        print("O cliente foi deletado \nEle não havia recebimentos!")
    else:
        arq_recibo = open(
            file='recebimentos.txt',
            mode='w',
            buffering=-1,
            encoding='utf-8',
            errors='replace'
        )

        arq_recibo.writelines(dados)
        arq_recibo.close()
        print("Cliente deletado\n Seus recibos também")
            


cod_cli = input("Digite o codigo do cliente para deletar: ")
excluir_cliente(cod_cli)