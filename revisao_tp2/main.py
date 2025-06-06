linhas = int(input("Digite o número de linhas da matriz: "))
colunas = int(input("Digite o número de colunas da matriz: "))

matriz_numeros=[]
for i in range(linhas):
	linha=[]
	matriz_numeros.append(linha)
	for j in range(colunas):
		numero=float(input(f"Digite o número para a posição ({i}, {j}): "))
		linha.append(numero)
	
	for linha in matriz_numeros:
		print(linha)