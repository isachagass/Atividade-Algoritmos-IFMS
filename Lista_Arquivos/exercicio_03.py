def verificacao_id(cod_cli):
    arq_clientes = open(
        file='clientes.txt',
        mode='r',
        buffering=-1,
        encoding='utf-8',
        errors='replace'
    )

    arq_clientes.readline()

    existe = False

    for linha in arq_clientes:
        dados = linha.strip().split(';')

        if len(dados) > 0 and dados[0] == cod_cli:
            existe = True
            break

    arq_clientes.close()
    return existe


arq_recebimentos = open(
    file='recebimentos.txt',
    mode='a',
    buffering=-1,
    encoding='utf-8',
    errors='replace'
)

print("Cadastro de recebimentos\n")

while True:
    num_doc = int(input("Digite o numero do documento - ou 0 para sair: "))

    if num_doc == 0:
        break

    cod_cli = input("Digite o codigo do cliente:")
    if not verificacao_id(cod_cli):
        print("Erro: Cliente não cadastrado")
        continue

    valor = float(input("Digite o valor do documento:"))
    data_emissao = input("Digite a data de emissão (DD/MM/AAAA):")
    data_vencimento = input("Digite a data de vencimento (DD/MM/AAAA):")

    dados = f'{num_doc};{valor};{data_emissao};{data_vencimento};{cod_cli}\n'
    arq_recebimentos.write(dados)
    print("Recebimento cadastrado\n")

arq_recebimentos.close()

