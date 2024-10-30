def formatacao_vendedor(vendedor):
    for dado in vendedor:
            if dado == 'endereco':
                print('Endereços: ')
                print('-----------------')
                for endereco in vendedor[dado]:
                    for item in endereco:
                        print(item.capitalize(), ':', endereco[item])
                    print('-----------------')
            if dado == 'produtos':
                print('Produtos: ')
                print('-----------------')
                for produto in vendedor[dado]:
                    for item in produto:
                        print(item.capitalize(), ':', produto[item])
                    print('-----------------')
            else:
                print(dado.capitalize() , ':', vendedor[dado]) 