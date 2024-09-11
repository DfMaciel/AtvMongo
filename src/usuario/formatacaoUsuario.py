def formatacao_usuario(usuario):
    for dado in usuario:
            if dado == 'endereco':
                print('Endereços: ')
                print('-----------------')
                for endereco in usuario[dado]:
                    for item in endereco:
                        print(item.capitalize(), ':', endereco[item])
                    print('-----------------')
            else:
                print(dado.capitalize() , ':', usuario[dado]) 