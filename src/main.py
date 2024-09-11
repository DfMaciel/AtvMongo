from conexao import conexao
from menus.menu import menu

conexao()
menu()

# def delete_usuario(nome, sobrenome):
#     #Delete
#     global db
#     mycol = db.usuario
#     myquery = {"nome": nome, "sobrenome":sobrenome}
#     mydoc = mycol.delete_one(myquery)
#     print("Deletado o usuário ",mydoc)

# def read_usuario(nome):
#     #Read
#     global db
#     mycol = db.usuario
#     print("Usuários existentes: ")
#     if not len(nome):
#         mydoc = mycol.find().sort("nome")
#         for x in mydoc:
#             print(x["nome"],x["cpf"])
#     else:
#         myquery = {"nome": nome}
#         mydoc = mycol.find(myquery)
#         for x in mydoc:
#             print(x)

# def update_usuario(nome):
#     #Read
#     global db
#     mycol = db.usuario
#     myquery = {"nome": nome}
#     mydoc = mycol.find_one(myquery)
#     print("Dados do usuário: ",mydoc)
#     nome = input("Mudar Nome:")
#     if len(nome):
#         mydoc["nome"] = nome

#     sobrenome = input("Mudar Sobrenome:")
#     if len(sobrenome):
#         mydoc["sobrenome"] = sobrenome

#     cpf = input("Mudar CPF:")
#     if len(cpf):
#         mydoc["cpf"] = cpf

#     newvalues = { "$set": mydoc }
#     mycol.update_one(myquery, newvalues)