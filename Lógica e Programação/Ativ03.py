def classificar_produto(preco, categoria):
    categoria = categoria.lower()  
    
    if categoria == "luxo":
        if preco > 1000:
            return "Premium"
        else:
            return "Padrão"
    
    elif categoria == "moda":
        if preco > 500:
            return "Padrão"
        elif preco < 200:
            return "Acessível"
        else:
            return "Padrão"
    
    elif categoria == "eletrônicos":
        if preco > 800:
            return "Premium"
        else:
            return "Padrão"
    
    else:
        return "Categoria desconhecida"

# Teste do programa
preco = float(input("Digite o preço do produto: R$ "))
categoria = input("Digite a categoria do produto (luxo, moda, eletrônicos): ")

classificacao = classificar_produto(preco, categoria)
print(f"O produto foi classificado como: {classificacao}")
