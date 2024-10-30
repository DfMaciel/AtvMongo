from conexao import db

def cadastrar_vendedor():
    global db
    mycol = db.vendedor
    print("\nInserindo um novo vendedor")
    nome = input("Nome: ")
    email = input("Email: ")
    senha = input("Senha: ")
    telefone = input("Telefone: ")
    continuar = True
    endereco = []
    produtos = []
    compras = []
    while (continuar):
        rua = input("Rua: ")
        numero = input("Num: ")
        bairro = input("Bairro: ")
        cidade = input("Cidade: ")
        estado = input("Estado: ")
        cep = input("CEP: ")
        endereco_inicial = {   
            "rua":rua,
            "numero": numero,
            "bairro": bairro,
            "cidade": cidade,
            "estado": estado,
            "cep": cep
        }
        endereco.append(endereco_inicial)
        key = input("Deseja cadastrar um novo endereço (S/N)? ")
        if key in ['N', 'n']:
            continuar = False
            break
        continuar2 = True
        while (continuar2):
            produto = input("Produto: ")
            descricao = input("Descrição: ")
            preco = input("Preço: ")
            estoque = input("Estoque: ")
            marca = input("Marca: ")
            produto_inicial = {   
                "produto":produto,
                "descricao": descricao,
                "preco": preco,
                "estoque": estoque,
                "marca": marca
            }
            produtos.append(produto_inicial)
            key = input("Deseja cadastrar um novo produto (S/N)? ")
            if key in ['N', 'n']:
                continuar2 = False
                break
        
    mydoc = { "nome": nome, "email": email, "senha": senha, "telefone": telefone, "endereco": endereco, "produtos": produto, "compras": compras}
    x = mycol.insert_one(mydoc)
    print("Documento inserido com ID ",x.inserted_id)