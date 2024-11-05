from vendedor.cadastrarVendedor import cadastrar_vendedor
from vendedor.listarVendedores import listar_vendedores
from vendedor.visualizarVendedor import visualizar_vendedor
from vendedor.atualizarVendedor import atualizar_vendedor
from vendedor.excluirVendedor import excluir_vendedor

def vendedor_menu():
    menu = True
    while (menu):
        opcao_usuario = 11
        print("Menu do vendedor")
        print("1-Cadastrar vendedor")
        print("2-Listar todos os vendedores")
        print("3-Verificar dados de um vendedor")
        print("4-Editar vendedor")
        print("5-Deletar vendedor")
        print("0-Voltar")
        opcao_usuario = input("Escolha uma opção: ")
        if (opcao_usuario == '1'):
            cadastrar_vendedor()
            
        elif (opcao_usuario == '2'):
            listar_vendedores()
        
        elif (opcao_usuario == '3'):
            id = input("Insira o ID do vendedor para ser visualizado: ")
            if (id):
                visualizar_vendedor(id)
            else: 
                print("ID inválido")

        elif (opcao_usuario == '4'):
            listar_vendedores()
            id = input("Insira o ID do vendedor para ser editado: ")
            if (id):
                atualizar_vendedor(id)
            else:
                print("ID inválido")

        elif (opcao_usuario == '5'):
            listar_vendedores()
            id = input("Insira o ID do vendedor para ser excluído: ")
            excluir_vendedor(id)
            
        elif (opcao_usuario == '0'):
            menu = False
            return
        else:
            print("Opção inválida!")
        break