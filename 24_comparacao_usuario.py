# Exercício 24: Crie duas variáveis com dois valores numéricos inteiros digitados pelo usuário,
# caso o valor do primeiro número for maior que o do segundo, exiba em tela uma mensagem de acordo,
# caso contrário, exiba em tela uma mensagem dizendo que o primeiro valor digitado é menor que o segundo

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if num1 > num2:
    print(f"O primeiro número ({num1}) é maior que o segundo ({num2})")
else:
    print(f"O primeiro número ({num1}) é menor que o segundo ({num2})")
