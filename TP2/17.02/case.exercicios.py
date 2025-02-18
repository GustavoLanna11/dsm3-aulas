#Estrutura condicional CASE
letra = str(input("Digite a letra do alfabeto: "))
match letra:
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