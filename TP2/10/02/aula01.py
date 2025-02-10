#valor = float(input("Digite o valor da compra: "))
#valortotal = valor * 10
#print(f"O valor total é {valortotal}")

# O f antes das aspas, serve para concatenar a variável e mostrá-la na tela normalmente.

#Arredondamento de valores
#print(f"área = {area:.2f} cm2")

#Teste 01
#nome = "Gustavo"
#idade = 29
#print("meu nome é " +nome)

#Exemplo 01
numero1 = int(input("Digite o primeiro valor: "))
numero2 = int(input("Digite o segundo valor: "))

resultado = numero1 + numero2
print(resultado)



#Exemplo 02
valorProduto = float(input("Digite o valor do produto: "))
valorDesconto = float(input("Digite o desconto em %: "))

valorDesconto = valorProduto * valorDesconto/100
valorVenda = valorProduto - valorDesconto

print(f"o valor final da venda é: {valorVenda}")