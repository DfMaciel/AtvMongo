from vendedor.formatacaoVendedor import formatacao_vendedor

def formatacao_produto(produto):
    for dado in produto:
        if dado == 'vendedor':
            print('Vendedor: ')
            print('-----------------')
            formatacao_vendedor(produto[dado])
            print('-----------------')
        else:
            print(dado.capitalize() , ':', produto[dado]) 
    print('-----------------')