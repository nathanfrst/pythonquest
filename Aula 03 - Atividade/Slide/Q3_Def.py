def desconto():
    valorProduto = float(input("Digite o valor do produto: "))
    desconto = valorProduto * 0.1
    valorFinal = valorProduto - desconto
    print(f"O valor final do produto com desconto é: {valorFinal}R$")

desconto()