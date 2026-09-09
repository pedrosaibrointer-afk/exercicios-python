# Exercício 25: Peça para que o usuário digite um número, em seguida exiba em tela uma mensagem
# dizendo se tal número é PAR ou se é ÍMPAR

numero = int(input("Digite um número: "))

if numero % 2 == 0:
    print(f"{numero} é um número PAR")
else:
    print(f"{numero} é um número ÍMPAR")
