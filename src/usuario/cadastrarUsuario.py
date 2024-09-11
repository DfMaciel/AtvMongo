from conexao import db

def cadastrar_usuario():
    global db
    mycol = db.usuario
    print("\nInserindo um novo usuário")
    nome = input("Nome: ")
    email = input("Email: ")
    senha = input("Senha: ")
    continuar = True
    endereco = []
    favoritos = []
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
    mydoc = { "nome": nome, "email": email, "senha": senha, "endereco": endereco, "favoritos": favoritos, "compras": compras}
    x = mycol.insert_one(mydoc)
    print("Documento inserido com ID ",x.inserted_id)