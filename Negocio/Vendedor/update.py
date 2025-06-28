from helpers.utils import find_address, register_address, find_seller, list_addresses

def update_seller(seller_id, sellerCol):
    seller = find_seller(seller_id, sellerCol)
    
    if not seller:
        return "Vendedor não encontrado!"

    novo_nome = input("Mudar Nome (ou Enter para manter): ")
    if novo_nome:
        seller["nome"] = novo_nome

    email = input("Mudar E-mail (ou Enter para manter): ")
    if email:
        seller["email"] = email
    
    nova_senha = input("Mudar Senha (ou Enter para manter): ")
    if nova_senha:
        seller["senha"] = nova_senha
        
    novo_telefone = input("Mudar Telefone (ou Enter para manter): ")
    if novo_telefone:
        seller["telefone"] = novo_telefone
    
   
    print("\n")
    print("Leia com atenção e escolha uma opção:")
    print("1 - Cadastrar novo endereço;")
    print("2 - Editar endereço existente;")
    print("3 - Remover endereço")
    print("4 - Próximo (não modificar endereço)")
    print("\n")
    opcao = int(input("Digite a opção escolhida: "))
    
    if opcao == 1:
        quantidade = int(input("Digite a quantidade de endereços que deseja cadastrar: "))
        c = 0
        while c < quantidade:
            novo_endereco = register_address(id, sellerCol, "VEND")
            sellerCol.update_one({"_id": seller["_id"]}, {"$push": {"endereco": novo_endereco}})
            c += 1
    
    elif opcao == 2:
        print("\n")
        cep = input("CEP do endereço que deseja editar: ")
        print("\n")
        index, address = find_address(cep, seller)
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
            nova_cidade = input("Nova Cidade (ou Enter para manter): ")
            if nova_cidade:
                address["cidade"] = nova_cidade
            novo_estado = input("Novo Estado (ou Enter para manter): ")
            if novo_estado:
                address["estado"] = novo_estado
            novo_cep = input("Novo CEP (ou Enter para manter): ")
            if novo_cep:
                address["cep"] = novo_cep
            sellerCol.update_one(
                {"_id": seller["_id"]},
                {"$set": {f"endereco.{index}": address}}
            )
            print("\n")
            print("Endereço atualizado com sucesso.")
            print("\n")
        else:
            print("Endereço não encontrado.")
    elif opcao == 3:
        list_address = list_addresses(seller)
        if not list_address:
            print("Sem endereços cadastrados.")
        print("\n")
        print("     Endereços cadastrados:")
        print("\n")
        for index, address in enumerate(list_address):
            print(f"Rua: {address.get('rua')}, Número: {address.get('numero')}, Bairro: {address.get('bairro')}, Cidade: {address.get('cidade')}, Estado: {address.get('estado')}, CEP: {address.get('cep')}")

        print("\n")
        cep = input("CEP do endereço que deseja remover: ")
        index, address = find_address(cep, seller)
        if index is not None:
            sellerCol.update_one({"_id": seller["_id"]},{"$pull": {"endereco": {"cep": cep}}})
            print("\n")
            print("Endereço removido.")
        else:
            print("Endereço não encontrado.")
    else:
        print("\n")
        print("Nenhuma mudança feita no endereço.")
    sellerCol.update_one({"_id": seller["_id"]}, {"$set": {"nome": seller["nome"], "email": seller["email"], "senha": seller["senha"], "telefone": seller["telefone"]}})
    print("\n")
    print("Dados atualizados com sucesso!")
