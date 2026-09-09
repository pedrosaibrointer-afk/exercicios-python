# Exercício 16: Escreva um programa que pede que o usuário dê entrada em dois valores,
# em seguida, exiba em tela o resultado da soma, subtração, multiplicação e divisão desses números

print("Digite dois números para realizar operações matemáticas")
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

soma = num1 + num2
subracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2

print(f"\nResultados:")
print(f"Soma: {num1} + {num2} = {soma}")
print(f"Subtração: {num1} - {num2} = {subracao}")
print(f"Multiplicação: {num1} * {num2} = {multiplicacao}")
print(f"Divisão: {num1} / {num2} = {divisao}")
