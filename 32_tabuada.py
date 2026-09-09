# Exercício 32: Crie um programa que exibe em tela a tabuada de um determinado número
# fornecido pelo usuário

numero = int(input("Digite um número para ver sua tabuada: "))

print(f"Tabuada do {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
