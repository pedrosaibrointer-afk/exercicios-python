# Exercício 34: Crie um programa que realiza a contagem de 1 até 100, usando apenas
# de números ímpares, ao final do processo exiba em tela quantos números ímpares foram
# encontrados nesse intervalo, assim como a soma dos mesmos

impares = []
soma = 0

for numero in range(1, 101):
    if numero % 2 != 0:
        impares.append(numero)
        soma += numero

print(f"Números ímpares de 1 a 100: {impares}")
print(f"Total de números ímpares: {len(impares)}")
print(f"Soma dos números ímpares: {soma}")
