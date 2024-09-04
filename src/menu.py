from usuario.cadastrarUsuario import cadastrar_usuario

def menu ():
    entrada = 11
    sair = True

    while (sair):
        print("Sistema de CRUD Mercado Livre")
        print("1-Usuário")
        print("2-Produto")
        print("3-Vendedor")
        print("4-Compra")
        print("0-Sair")
        entrada = input("Escolha uma opção: ")

        if (entrada == '1'):
            opcao_usuario = 11
            print("Menu do Usuário")
            print("1-Cadastrar usuário")
            print("2-Listar todos os usuários")
            print("3-Verificar dados de um usuário")
            print("4-Editar usuário")
            print("5-Deletar usuário")
            print("0-Voltar")
            opcao_usuario = input("Escolha uma opção: ")
            if (opcao_usuario == '1'):
                cadastrar_usuario()
                
            elif (opcao_usuario == '2'):
                nome = input("Read usuário, deseja algum nome especifico? ")
                read_usuario(nome)
            
            elif (opcao_usuario == '3'):
                nome = input("Update usuário, deseja algum nome especifico? ")
                update_usuario(nome)

            elif (opcao_usuario == '4'):
                print("delete usuario")
                nome = input("Nome a ser deletado: ")
                sobrenome = input("Sobrenome a ser deletado: ")
                delete_usuario(nome, sobrenome)
                
        elif (input == '2'):
            opcao_usuario = 11
            print("Menu do Vendedor")   
            print("1-Cadastrar vendedor")
            print("2-Listar todos os vendedores")
            print("3-Verificar dados de um vendedor")
            print("4-Editar vendedor")
            print("5-Deletar vendedor")
            print("0-Voltar")
        elif (input == '3'):
            opcao_usuario = 11
            print("Menu do Produto") 
            print("1-Cadastrar produto")
            print("2-Listar todos os produtos")
            print("3-Verificar dados de produto")
            print("4-Editar produto")
            print("5-Deletar produto") 
            print("0-Voltar")
        elif (input == '4'):
            opcao_usuario = 11
            print("Menu de Compra")
            print("1-Realizar uma compra")
            print("2-Listar todas as compras")
            print("3-Editar uma compra")
            print("4-Excluir uma compra")
            print("0-Voltar")
        elif (input == '0'):
            sair = False
        else: 
            print("Opção inválida!")      

    print("Tchau Prof...")
