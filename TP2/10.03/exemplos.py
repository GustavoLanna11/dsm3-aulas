# Vetor e matriz são coleções de variáveis contínuas na memória e acessadas através de um número de índice. A diferença entre vetores e matrizes é que vetores são em uma única dimensão, enquanto matrizes, várias.

#Vetor 
vetor = [10,20,30,40,50]
print(vetor)

#Exemplo 1 - pip install numpy - biblioteca para fazer calculo de matrizes
import numpy as np
tamanho = int(input("Digite o tamanho do vetor: "))
1
vetor = np.empty(tamanho, dtype=int)

for i in range(tamanho):
    elemento = int(input(f"Digite o elemento {i+1} do vetor: "))
    vetor[i] = elemento
print("Vetor: ", vetor)


# Split - divide um string em diversos itens dentro de um vetor
frase = "Isso é uma frase de exemplo"
palavras = frase.split()
# resultado: ['isso', 'é', 'uma', 'frase', 'de', 'exemplo']

#exemplo split
frase = "Essa é uma frase em Python"
palavras = frase.split()
print(palavras)

#Exemplo split 2:
entrada = input("Digite os elementos do vetor, separados por espaços: ")
vetor = [int(x) for x in entrada.split()]
print("Vetor:", vetor)

#########################################################

# Matriz estática, com elementos já definidos
matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print("Elemento na primeira linha e primeira coluna: ", matriz[0][0])
print("Elemento na segunda linha e terceira coluna: ", matriz[1][2])
print("Elemento na terceira linha e segunda coluna: ", matriz[2][1])

print("Matriz:")
for linha in matriz:
    print(linha)

#Matriz com dados do usuário
linhas = int(input("Digite um número de linhas da matriz: "))
colunas = int(input("Digite o número de colunas da matriz: "))
matriz_numeros = []
for i in range(linhas):
    linha = []
    matriz_numeros.append(linha)
    for j in range(colunas):
        numero = float(input(f"Digite o número para a posição ({i},{j}): "))
        linha.append(numero)

for linha in matriz_numeros:
    print(' '.join(map(str, linha)))