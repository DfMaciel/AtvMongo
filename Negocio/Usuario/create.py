def create_user(userCol):
    print("\nInserindo um novo usuário")
    nome = input("Nome: ")
    email = input("E-mail: ")
    senha = input("Senha: ")
    key = 1
    end = []
    favoritos =[]
    compras = []
    while (key != 'n' and key != "nao"):
        cep = input("CEP: ")
        rua = input("Rua: ")
        numero = input("Número da casa: ")
        bairro = input("Bairro: ")
        cidade = input("Cidade: ")
        estado = input("Estado: ")
        endereco = {        
            "rua":rua,
            "numero": numero,
            "bairro": bairro,
            "cidade": cidade,
            "estado": estado,
            "cep": cep
        }
        end.append(endereco) 
        key = input("Deseja cadastrar um novo endereço (S/N)? ").lower()
    mydoc = { "nome": nome, "email": email, "endereco": end, "senha": senha, "favoritos": favoritos, "compras": compras }
    x = userCol.insert_one(mydoc)
    print("Documento inserido com ID ",x.inserted_id)
