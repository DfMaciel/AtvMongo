def formatacao_usuario(usuario):
    for dado in usuario:
            if dado == 'endereco':
                print('Endereços: ')
                print('-----------------')
                for endereco in usuario[dado]:
                    for item in endereco:
                        print(item.capitalize(), ':', endereco[item])
                    print('-----------------')
            elif dado == 'favoritos':
                print('Favoritos: ')
                print('-----------------')
                for favorito in usuario[dado]:
                    for item in favorito:
                        print(item.capitalize(), ':', favorito[item])
                    print('-----------------')
            else:
                print(dado.capitalize() , ':', usuario[dado]) 
    print('-----------------')