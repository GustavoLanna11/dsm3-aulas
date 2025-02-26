#Exercício 1
from datetime import datetime
anoNasc = int(input("Digite seu ano de nascimento: "))
anoAtual = datetime.now().year
idade = anoAtual - anoNasc
print(f"Sua idade é: {idade}")

if idade >= 16:
    print("Pode votar!")
else:
    print("Não pode votar!")

#Exercício 2
metros = int(input("Digite uma medida: "))
menu = int(input("Escolha uma conversão para essa medida: 1 - Decímetros | 2 - Centímetros | 3 -Milimetros"))
match menu:
    case 1:
        decimetros = metros * 10.0
        print(f"O valor digitado em decimetros é: {decimetros}")
    case 2:
        centimetros = metros * 100.0
        print(f"O valor digitado em centímetros é: {centimetros}")
    case 3:
        milimetros = metros * 1000.0
        print(f"O valor digitado em milímetros é: {milimetros}")
    case _:
        print("Opção inválida!")

#Exercício 3
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
simbolo = str(input("Digite um símbolo de operação matemática básica (+, -, * ou /): "))
match simbolo:
    case "+":
        resultado = num1 + num2
        print(f"O resultado da soma dos números é: {resultado}")
    case "-":
        resultado = num1 - num2
        print(f"O resultado da subtração entre os dois números é: {resultado}")
    case "*":
        resultado = num1 * num2
        print(f"O resultado da multiplicação entre os dois números é: {resultado}")
    case "/":
        resultado = num1 / num2
        print(f"O resultado da divisão entre os dois números é: {resultado}")
    case _:
        print("Opção inválida")

#Exercício 4
num1 = int(input(""))