arq_clientes = open(
    file='clientes.txt',
    mode='w',
    buffering=-1, 
    encoding='utf-8',
    errors='replace' 
)
arq_clientes.write('Cod_Cli;Nome;Endereco;Fone\n')
arq_clientes.close() 

arq_recebimentos = open(
    file= 'recebimentos.txt',
    mode= 'w',
    buffering=-1,
    encoding='utf-8',
    errors='replace'
)
arq_recebimentos.write('Num_doc;Valor_doc;Data_Emissao;Data_Vencimento;Cod_Cli\n')
arq_recebimentos.close()
print("Documentos criados!")