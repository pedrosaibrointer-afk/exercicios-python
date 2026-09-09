# Exercício 28: Crie uma lista com 8 elementos de uma lista de compras de supermercado,
# por meio de um laço de repetição for liste individualmente cada um dos itens dessa lista

lista_compras = ["Leite", "Pão", "Ovos", "Maçã", "Arroz", "Feijão", "Açúcar", "Sal"]

print("Lista de Compras:")
for i, item in enumerate(lista_compras, 1):
    print(f"{i}. {item}")
