#Exercício 1
num = 0
while num <= 100:
    print (num)
    num += 1

#Exercício 2
num = int(input("Digite um número: "))
cont = 0
while cont <= num:
    print(cont)
    cont += 1

#Execício 3
num = int(input("Digite um número: "))
cont = 1
while cont<= 10:
    print(f"{num} * {cont} = {(cont * num)}")
    cont += 1

#Exercício 4
num = int(input("Digite um número: "))
inicio = int(input("Digite o inicio da tabuada: "))
fim = int(input("Digite o fim da tabuada: "))

cont = inicio
while cont<= fim:
    print(f"{num} * {cont} = {(cont * num)}")
    cont += 1


#Exercício 5
resposta1 = str(input("Digite a resposta da questão 1 : "))
resposta2 = str(input("Digite a resposta da questão 2 : "))
resposta3 = str(input("Digite a resposta da questão 3 : "))
if resposta1 == "a":
    print("+1")
elif resposta1 != "a":
    print("+0")

if resposta2 == "c":
    print("+1")
elif resposta2 != "c":
    print("+0")

if resposta3 == "d":
    print("+1")
elif resposta3 != "d":
    print("+0")

while resposta1 == "a" and resposta2 == "c" and resposta3 == "d":
    print("Você possui 3 pontos")
    break
while resposta1 != "a" and resposta2 != "c" and resposta3 != "d":
    print("Você possui 0 pontos")
    break
while resposta1 == "a" or resposta2 != "c" or resposta3 != "d":
    print("Você possui 1 pontos")
    break
while resposta1 == "a" and resposta2 != "c" or resposta3 != "d" and resposta1 == "a" or resposta3 != "d" and resposta2 != "c":
    print("Você possui 2 pontos")
    break

#Exercício 6
valor = 1.99
print("Lojas quase dois = tabela de preços")
for i in range (1, 51):
    print(f"{i} - R$ {(valor * i):.2f}")

#Exercício 7
valor = 0.54
print("Pão de ontem - Tabela de preços")
for i in range (2, 51, 2):
    print(f"{i} - R$ {(valor * i):.2f}")

#Exercício 8
print("Lojas luiz")
produto = 1
total = 0
i = 1
while produto != 0:
    produto = int(input(f"Produto {i}: "))
    total += produto
    i += 1
    print(total)

#Exercício 10
