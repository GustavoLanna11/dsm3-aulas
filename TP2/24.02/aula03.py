# Estruturas de repetição

# Tipos de LOOP: 
# - for (sequência, lista, executa um bloco para cada elemento da sequência);
# - while (executa um código enquanto a condição for verdadeira).

# Python oferece controle de fluxo com "break" e "continue".

# Exemplo com while
count = 5
while count > 0:
    print(count)
    # Decrementando
    count -= 1

# For
for i in range (2, 11, 2):
    print(i)

# Exemplo com array
localizar = "banana"
fruits = ["Maçã", "banana", "laranja"]
for fruit in fruits:
    if fruit == localizar:
        print(f"Encontrado: {localizar}")
        break
    else: 
        print(f"{localizar} não encontrado")

