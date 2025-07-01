from helpers.utils import find_user, find_address, register_address, list_addresses

def update_user(id, usuarioCol):
    user = find_user(id, usuarioCol)
    if not user:
        print("Usuário não encontrado!")
        return
    
    print(f"Nome atual: {user.get('nome')}")
    novo_nome = input("Mudar Nome (ou Enter para manter): ")
    
    print(f"Email atual: {user.get('email')}")
    email = input("Mudar E-mail (ou Enter para manter): ")
    print("\n")
    print(" Escolha uma opção: ")
    print("1 - Cadastrar novo endereço;")
    print("2 - Editar endereço existente;")
    print("3 - Remover endereço existente;")
    print("4 - Próximo (não modificar endereço)")
    print("\n")

    try:
        opcao = int(input("Digite a opção escolhida: "))
    except ValueError:
        print("Opção inválida!")
        return
    if opcao == 1:
        quantidade = int(input("Digite a quantidade de endereços que deseja cadastrar: "))
        c = 0
        while c < quantidade:
            novo_endereco = register_address(id, usuarioCol, "USER")
            usuarioCol.update_one({"_id": user["_id"]}, {"$push": {"endereco": novo_endereco}})
            c += 1
    elif opcao == 2:
        cep = input("Digite o CEP do endereço que deseja editar: ")
        index, address = find_address(cep, user)
        if address is not None:
            nova_rua = input("Nova Rua (ou Enter para manter): ")
            if nova_rua:
                address["rua"] = nova_rua
            novo_numero = input("Novo Número (ou Enter para manter): ")
            if novo_numero:
                address["numero"] = novo_numero
            novo_bairro = input("Novo Bairro (ou Enter para manter): ")
            if novo_bairro:
                address["bairro"] = novo_bairro
            nova_cidade = input("Novo Cidade (ou Enter para manter): ")
            if nova_cidade:
                address["cidade"] = nova_cidade
            novo_estado = input("Novo estado (ou Enter para manter): ")
            if novo_estado:
                address["estado"] = novo_estado
            usuarioCol.update_one(
                {"_id": user["_id"]},
                {"$set": {f"endereco.{index}": address}}
            )
            print("\n")
            print("Endereço atualizado com sucesso.")
            print("\n")
        else:
            print("Endereço não encontrado.")
    elif opcao == 3:
        addresses = list_addresses(user)
        if not addresses:
            return print("Sem endereços cadastrados.")
        print("\n")
        print("     Endereços cadastrados:")
        print("\n")
        for address in addresses:
            print(f"Rua: {address.get('rua')}, Número: {address.get('numero')}, Bairro: {address.get('bairro')}, Cidade: {address.get('cidade')}, Estado: {address.get('estado')}, CEP: {address.get('cep')}")
        print("\n")
        cep = input("CEP do endereço que deseja remover: ")
        index, address = find_address(cep, user)
        if index is not None:
            usuarioCol.update_one({"_id": user["_id"]},{"$pull": {"endereco": {"cep": cep}}})
            print("Endereço removido com sucesso.")
        else:
            print("Endereço não encontrado.")
    else:
        print("\n")
        print("Nenhuma mudança feita no endereço.")
    
    # Atualizar os campos do usuário no banco de dados
    update_fields = {}
    if novo_nome:
        update_fields["nome"] = novo_nome
    if email:
        update_fields["email"] = email
    
    if update_fields:
        usuarioCol.update_one({"_id": user["_id"]}, {"$set": update_fields})
        print("\n")
        print("Dados atualizados com sucesso!")
    else:
        print("\n")
        print("Nenhuma alteração foi feita nos dados do usuário.")
