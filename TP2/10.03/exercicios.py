# Exercício 1
vetor = []
for i in range (10):
    numero = int(input(f"Digie o {i+1} número: "))
    vetor.append(numero)

print("Os números digitados são: ", vetor)

#Exercício 2
matriz = []
for i in range(4):
    linha = []
    matriz.append(linha)
    for j in range(4):
        numero = int(input("Digite o numero da posição ({i}, {j}): "))
        linha.append(numero)
        if numero > 10:
            quantidade +=1 
print(f"Quantidade de numero maior que 10 é: {quantidade}")
for i in range(4):
    print(matriz[i])

#Exercício 3

#Exercício 4
vetor_cor = []
for i in range (5):
    cor = str(input(f"Digite a {i+1} cor: "))
    vetor_cor.append(cor)
print("As cores digitadas são: ", vetor_cor)

#Exercício 5
