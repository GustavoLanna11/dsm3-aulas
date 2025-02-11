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
