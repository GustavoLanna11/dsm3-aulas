#Estrutura condicional IF e Else

# Exercício 1
nome1 = str(input("Digite o nome da primeira pessoa: "))
nome2 = str(input("Digite o nome da segunda pessoa: "))
peso1 = float(input("Digite o peso da primeira pessoa: "))
peso2 = float(input("Digite o peso da segunda pessoa: "))

if peso1 > peso2:
    print(f"A pessoa mais pesada é: {nome1}")
    print(f"O peso dela é: {peso1}")
elif peso2 > peso1:
    print(f"A pessoa mais pesada é: {nome2}")
    print(f"O peso dela é: {peso2}")
else:
    print(f"As duas pessoas tem o mesmo peso: {peso1}, {peso2}, respectivamente.")


#Exercício 2
valor = int(input("Digite um valor inteiro: "))
validacao = valor % 2
if validacao == 0:
    print(f"O valor digitado é par: {valor}")
    quadrado = valor * valor
    print(f"O valor digitado ao quadrado é: {quadrado}") 
elif validacao != 0:
    print(f"O valor digitado é ímpar: {valor}")
    cubo = valor * valor * valor
    print(f"O valor digitado ao cubo é: {cubo}")


#Exercício 3
estatura1 = float(input("Digite a primeira altura: "))
estatura2 = float(input("Digite a segunda altura: "))
estatura3 = float(input("Digite a terceira altura: "))

vetorValores = [estatura1, estatura2, estatura3]
vetorValores.sort(reverse=True)
print(f"A lista de valores em ordem decrescente é: {vetorValores}")


#Exercício 4
num1 = int(input("Digite o primeiro valor: "))
num2 = int(input("Digite o segundo valor: "))

valorMenu = int(input("***Menu*** | 1 - Média ponderada, com peso 2 e 3, respectivamente | 2 - Quadrado da soma dos 2 números | 3 - Cubo do menor número /n Escolha uma opção!"))
if valorMenu == 1:
    mediaPonderada = (num1 * 2) + (num2 * 3)
    print(f"A média ponderada de {num1} e {num2} é: {mediaPonderada}")

elif valorMenu == 2:
    somaNumero = num1 + num2
    quadradoSoma = somaNumero * somaNumero
    print(f"A soma dos dois números é: {somaNumero} e quadrado da soma dos dois números é: {quadradoSoma}") 

elif valorMenu == 3:
    if num1 < num2:
        cuboMenor = num1 * num1 * num1
        print(f"O cubo do menor número é: {cuboMenor}")
    elif num2 < num1:
        cuboMenor = num2 * num2 * num2
        print(f"O cubo do menor número é: {cuboMenor}")
    elif num1 == num2:
        cuboMenor = num1 * num1 * num1
        print(f"Os números são iguais, e o cubo é: {cuboMenor}")

elif valorMenu == 0 or valorMenu > 3:
    print("Valor de menu inválido.")


