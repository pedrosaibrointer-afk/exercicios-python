# Exercício 29: Crie um programa que lê um valor de início e um valor de fim,
# exibindo em tela a contagem dos números dentro desse intervalo

inicio = int(input("Digite o valor de início: "))
fim = int(input("Digite o valor de fim: "))

print(f"Contagem de {inicio} a {fim}:")
for numero in range(inicio, fim + 1):
    print(numero, end=" ")
print()
