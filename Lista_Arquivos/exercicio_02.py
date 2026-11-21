arq_clientes = open(
    file= 'clientes.txt',
    mode='a',
    buffering=-1,
    encoding='utf-8',
    errors='replace'
)

print("Cadastro de clientes\n")

while True:
    cod_cli = input("Digite o código do cliente - ou 0 para sair: ")

    if cod_cli == '0':
        break

    nome = input("Digite o nome: ")
    endereco = input("Digite o endereço: ")
    fone = input("Digite o numero de telefone: ")

    dados = f'{cod_cli};{nome};{endereco};{fone}\n'
    arq_clientes.write(dados)
    print("Cliente cadastrado!")

arq_clientes.close()