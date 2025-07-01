def list_favorite(user):
    favorites = user.get("favoritos", [])
    
    if not favorites:
        print("\nSua lista de favoritos está vazia.")
        return
    
    print("\nSeus produtos favoritos:")
    print("-" * 50)
    
    for index, product in enumerate(favorites, 1):
        print(f"{index}. {product.get('produto', 'N/A')} - {product.get('marca', 'N/A')}")
        print(f"   Preço: R$ {float(product.get('preco', 0)):.2f}")
        print("-" * 50)
