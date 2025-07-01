from helpers.utils import find_purchases

def update_purchase(user, userCol, nota_fiscal, purCol):
    print("\n")
    print("     Atualizar Compra")
    print("\n")
    purchase = find_purchases(nota_fiscal, purCol)
    if not purchase:
        print("\n")
        print("Compra não encontrada.")
        print("\n")
        return
    new_status = input("Digite o novo status: ")

    purCol.update_one({"nota_fiscal": nota_fiscal},{"$set": {"status": new_status}})

    userCol.update_one({"_id": user["_id"], "compras.nota_fiscal": nota_fiscal},{"$set": {"compras.$.status": new_status}})
    print("\n")
    print("      Status de entrega atualizado!")
    print("\n")
