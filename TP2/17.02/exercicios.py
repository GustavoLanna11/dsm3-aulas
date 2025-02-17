#Exercício 1
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