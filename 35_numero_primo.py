# Exercício 35: Crie um programa que pede ao usuário que o mesmo digite um número qualquer,
# em seguida retorne se esse número é primo ou não, caso não, retorne também quantas vezes
# esse número é divisível

numero = int(input("Digite um número: "))
contador_divisores = 0
divisores = []

for i in range(1, numero + 1):
    if numero % i == 0:
        contador_divisores += 1
        divisores.append(i)

if contador_divisores == 2:
    print(f"{numero} é um número PRIMO")
else:
    print(f"{numero} NÃO É um número primo")
    print(f"Divisores de {numero}: {divisores}")
    print(f"{numero} é divisível {contador_divisores} vezes")
