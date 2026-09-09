# Exercício 8: Peça para que o usuário digite um número, em seguida o converta para float,
# exibindo em tela tanto o número em si quanto seu tipo de dado

numero = input("Digite um número: ")
numero_float = float(numero)

print(f"Número: {numero_float}")
print(f"Tipo de dado: {type(numero_float)}")
