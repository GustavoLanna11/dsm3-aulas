#Exercício 1
altura = float(input("Digite sua altura: "))
altura = altura * 100
print(f"Sua altura em cm é: {altura}")

#Exercício 2
deslocamento = int(input("Digite a distância percorrida: "))
tempo = int(input("Digite o tempo em segundos: "))
vm = deslocamento/tempo
print(f"A velocidade média do objeto é: {vm}")

#Exercício 3
raio = float(input("Digite o valor do raio: "))
area = (3.14 * (raio*raio))
print(f"O valor da area é: {area}")

#Exercício 4
altura = float(input("Digite a altura: "))
base = float(input("Digite a base: "))
area = (base*altura)/2
print(f"O valor da area é: {area}")

#Exercício 5
numero1 = int(input("Digite o valor do primeiro número: "))
numero2 = int(input("Digite o valor do segundo número: "))

adicao = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2
divisao = numero1 / numero2

print(f"O resultado da adição dos números é: {adicao}")
print(f"O resultado da subtração dos números é: {subtracao}")
print(f"O resultado da multiplicação dos números é: {multiplicacao}")
print(f"O resultado da divisão dos números é: {divisao}")

#Exercício 6
salario = float(input("Digite o salário mensal: "))
reajuste = int(input("Digite o percentual de reajuste"))
reajuste = salario * reajuste / 100
salario = salario + reajuste
print(f"O valor do salario pós reajuste é: ")

#Exercício 7
nome = str(input("Digite seu nome: "))
idade = int(input("Digite a idade:"))
diasVividos = idade * 365
print(f"Seus dias vividos são: {diasVividos}")

#Exercício 8
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro número: "))

soma = numero1 + numero2 + numero3
somaQuadrado = soma * soma
print(f"O valor da soma dos 3 exercícios ao quadrado é: {somaQuadrado}")

#Exercício 9
votosBrancos = int(input("Digite o valor de votos brancos: "))
votosNulos = int(input("Digite o valor de votos nulos: "))
votosValidos = int(input("Digite o valor de votos válidos: "))
total = votosBrancos + votosNulos + votosValidos

perbrancos = (votosBrancos * 100)/total
pernulos = (votosNulos * 100)/total
pervalidos = (votosValidos * 100)/total

print(f"O percentual de votos brancos é: {perbrancos}")
print(f"O percentual de votos nulos é: {pernulos}")
print(f"O percentual de votos validos é: {pervalidos}")
print(f"Total de votos é: {total}")

#Exercício 10
raio = float(input("Digite o valor do raio: "))
altura = float(input("Digite o valor da altura: "))
volume = (3.14 * (raio*raio) * altura)
print(f"o valor do volume é: {volume}")



#Exercício 11
descricao =str(input("Digite a descrição do produto: "))
qtdComprada = int(input("Digite a quantidade comprada: "))
valorUnitario = float(input("Digite o valor unitário do produto: "))
total = qtdComprada * valorUnitario

print(f"O total dos produtos é: {total}")
print(f"A descrição do produto é: {descricao}")
