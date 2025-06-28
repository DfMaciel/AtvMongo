from helpers.utils import find_user
def delete_user(_id, userCol):
    user = find_user(_id, userCol)
    if user:
        userCol.delete_one({"_id":user["_id"]})
        return print("Usuario excluido!")
    return print("Usuario não encontrado!")