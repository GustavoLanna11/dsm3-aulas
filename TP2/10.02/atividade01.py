


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