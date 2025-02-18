#Estrutura condicional - IF Else
nota1 = int(input("Digite sua primeira nota: "))
nota2 = int(input("Digite sua segunda nota: "))
media = (nota1 + nota2)/2
if media > 6:
    print("Aprovado")
else:
    print("Reprovado")

#Estrutura condicional - Case
opcao = int(input("1 - sacar | 2 - extrato | 3 - sair | Escolha uma opção"))
match opcao:
    case 1:
        print("Escolheu a opção sacar")
        valor = float(input("Digite o valor do saque: R$:"))
        print(f"Sacando da sua conta o valor de {valor}...")
    case 2:
        print("Escolheu a opção extrato")
        dias = int(input("Digite a quantidade de dias do extrato R$: "))
        print(f"Retirando o extrato de {dias} dias...")
    case 3: 
        exit
    case _:
        print("Opção inválida")