import uuid
from bson.objectid import ObjectId

def find_seller(seller_id, collection):
    #busca vendedor por ObjectId
    try:
        myquery = {"_id": ObjectId(seller_id)}
        mydoc = collection.find_one(myquery)
        return mydoc
    except:
        return None

def find_product(productId, productCol):
    # Busca o produto
    myquery = {"_id": ObjectId(productId)}
    product = productCol.find_one(myquery)
    return product  

def find_user(user_id, collection):
    #busca cliente por ObjectId
    try:
        myquery = {"_id": ObjectId(user_id)}
        mydoc = collection.find_one(myquery)
        return mydoc
    except:
        return None

def find_purchases(notaFiscal, collection):
    #busca compra
    myquery = {"nota_fiscal": notaFiscal}
    mydoc = collection.find_one(myquery)
    return mydoc
    
def find_address(cep, user):
    enderecos = user.get("endereco", [])
    for i, address in enumerate(enderecos):
        if (address.get("cep") == cep):
            return i, address  
    return None, None

def register_address(id, collection, tipo):
    if tipo == "VEND":
        user = find_seller(id, collection)
    if tipo == "USER":
        user = find_user(id,collection)
    if user:
        rua = input("Rua: ")
        numero = input("Número: ")
        bairro = input("Bairro: ")
        cidade = input("Cidade: ")
        estado = input("Estado: ")
        cep = input("CEP: ")
        endereco = {        
            "rua":rua,
            "numero": numero,
            "bairro": bairro,
            "cidade": cidade,
            "estado": estado,
            "cep": cep
        }
        return endereco

def list_addresses(user):
    addresses = user.get("endereco", [])
    if not addresses:
        print("\nNão existem endereços cadastrados!\n")
        return None
    return addresses

def generate_nota_fical():
    return str(uuid.uuid4())

def calculate_final_value(product, quantity):
    value_product = float(product.get("preco"))
    final_value = value_product * quantity
    return round(final_value, 2)







    
