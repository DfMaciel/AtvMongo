def create_seller(sellerCol):
    print("\n")
    print(" Inserindo um novo vendedor")
    print("\n")
    nome = input("Nome: ")
    email = input("E-mail: ")
    senha = input("Senha: ")
    telefone = input("Telefone: ")
    key = 1
    endereco = []
    produtos = []
    compras = []
    while (key != 'n'):
        rua = input("Rua: ")
        numero = input("Número: ")
        bairro = input("Bairro: ")
        cidade = input("Cidade: ")
        estado = input("Estado: ")
        cep = input("CEP: ")
        end = {        
            "rua": rua,
            "numero": numero,
            "bairro": bairro,
            "cidade": cidade,
            "estado": estado,
            "cep": cep
        }
        endereco.append(end) 
        key = input("Deseja cadastrar um novo endereço (S/N)? ").lower()
    mydoc = { "nome": nome, "email": email, "senha": senha, "telefone": telefone, "endereco": endereco, "produtos": produtos, "compras": compras}
    x = sellerCol.insert_one(mydoc)
    print("\n")
    print("Documento inserido com ID ",x.inserted_id)