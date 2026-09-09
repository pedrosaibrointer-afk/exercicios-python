# Exercício 36: Crie um programa que pede que o usuário digite um nome ou uma frase,
# verifique se esse conteúdo digitado é um palíndromo ou não, exibindo em tela esse resultado

texto = input("Digite um nome ou frase: ").replace(" ", "").lower()
texto_invertido = texto[::-1]

if texto == texto_invertido:
    print(f"'{texto}' É um PALÍNDROMO")
else:
    print(f"'{texto}' NÃO É um palíndromo")
