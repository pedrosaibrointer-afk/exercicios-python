# Exercício 31: Crie um programa que realiza a Progressão Aritmética de 20 elementos,
# com primeiro termo e razão definidos pelo usuário

primeiro_termo = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))

print("Progressão Aritmética:")
for i in range(20):
    termo = primeiro_termo + (i * razao)
    print(termo, end=" ")
print()
