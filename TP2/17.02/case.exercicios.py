#Estrutura condicional CASE

#Exercício 1
letra = str(input("Digite a letra do alfabeto: "))
match letra.lower():
    case "a":
        print("é uma vogal!")
    case "e":
        print("é uma vogal!")
    case "i":
        print("é uma vogal!")
    case "o":
        print("é uma vogal!")
    case "i":
        print("é uma vogal!")
    case _:
        print("É uma consoante!")


#Exercício 2
indice = int(input("Digite o indíce de poluição:"))
match indice:
    case 0 | 1 | 2:
        print("Aaceitável")
    case 3 | 4 | 5:
        print("Suspender Atividades - Grupo 1")
    case 6 | 7:
        print("Suspender atividades - Grupo 1 e 2")
    case _:
        print("Suspender as atividades de todos os grupos")


#Exercício 3
u = float(input("Digite o valor de U: "))
r = float(input("Digite o valor de R: "))
i = float(input("Digite o valor de I: "))

menu = int(input("1 - Tensão | 2 - Resistência | 3 - Corrente | Escolha um"))
match menu:
    case 1:
        u = r * i
        print(f"A tensão é: {u}")
    case 2: 
        r = u/i
        print(f"A resistência é: {r}")
    case 3:
        i = u/r
        print(f"A corrente é: {i}")
    case _:
        print("Inválido.")

#Exercício 4
precoInicial = float(input("Digite o valor inicial da compra: "))
pagamento = int(input(" 1 - à vista em espécie | 2 - cartão de débito | 3 - cartão de crédito | Escolha uma opção"))

match pagamento:
    case 1:
        print("À vista e em espécie")
        desconto = (precoInicial * 15)/100
        precoFinal = precoInicial - desconto

        print(f"Preço inicial: {precoInicial}")
        print(f"O desconto é de: {desconto}")
        print(f"O preço com desconto é: {precoFinal}")
    case 2: 
        print("Cartão de débito")
        desconto = (precoInicial * 10)/100
        precoFinal = precoInicial - desconto

        print(f"Preço inicial: {precoInicial}")
        print(f"O desconto é de: {desconto}")
        print(f"O preço com desconto é: {precoFinal}")
    case 3: 
        print("Cartão de crédito")
        desconto = (precoInicial * 5)/100
        precoFinal = precoInicial - desconto
        
        print(f"Preço inicial: {precoInicial}")
        print(f"O desconto é de: {desconto}")
        print(f"O preço com desconto é: {precoFinal}")
    
    # Falta o exercício 5 e 6, estão no slide da aula!