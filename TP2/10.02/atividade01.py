#Exercício 1
print("Olá, vendedor! Seu salário fixo é: R$ 1500, mais R$50 de bônus por software vendido!")
qtdSoftwareVendido = int(input("Digite a quantidade de softwares vendidos: "))
bonusSoftware = qtdSoftwareVendido * 50
salario = 1500 + bonusSoftware
print(f"Seu salário final é de: {salario}")

#Exercício 2
valorPrestacao = float(input("Digite o valor da prestação: "))
taxaJuros = int(input("Digite a taxa de juros imposta pelo banco: "))
tempo = int(input("Digite a quantidade de meses em atraso: "))

valorAtraso = valorPrestacao + (valorPrestacao*(taxaJuros/100)*100)
print(f"O valor da prestação em atraso é: {valorAtraso}")

#Exercício 3
temperaturaC = int(input("Digite a temperatura em Celsius: "))
temperaturaF = temperaturaC * 1.8 + 32
print(f"A temperatura {temperaturaC} graus Celsius passada para graus Fahrenheit é: {temperaturaF}")

#Exercício 4
from datetime import datetime
anoNasc = int(input("Digite seu ano de nascimento: "))
nome = str(input("Digite seu nome: "))

anoAtual = datetime.now().year
idade = anoAtual - anoNasc
print(f"O nome da pessoa é: {nome}")
print(f"A idade da pessoa é: {idade}")

#Exercício 5
