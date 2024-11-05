from vendedor.formatacaoVendedor import formatacao_vendedor

def formatacao_produto(produto):
    for dado in produto:
        print(dado.capitalize() , ':', produto[dado]) 
        if dado == 'vendedor':
            print('Vendedor: ')
            print('-----------------')
            formatacao_vendedor(produto[dado])