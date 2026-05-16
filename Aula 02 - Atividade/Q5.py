feijaoPreco = 8
arrozPreco = 6.5
farinhaPreco = 5
vendasTotal = 0

confirmacao = str(input("Deseja iniciar o programa? (S/N) ")).upper()

while confirmacao == "S":
    vendas = int(input("Digite o número de vendas: "))
    vendasTotal += vendas

    comprasFeijao = int(input("Digite a quantidade de pacotes de feijão comprado: "))
    comprasArroz = int(input("Digite a quantidade de pacotes de arroz comprado: "))
    comprasFarinha = int(input("Digite a quantidade de pacotes de farinha comprado: "))

    totalFeijao = comprasFeijao * feijaoPreco
    totalArroz = comprasArroz * arrozPreco
    totalFarinha = comprasFarinha * farinhaPreco

    print(f"Total ganho com feijão: R${totalFeijao:.2f}")
    print(f"Total ganho com arroz: R${totalArroz:.2f}")
    print(f"Total ganho com farinha: R${totalFarinha:.2f}")
    print(f"Número total de vendas: {vendasTotal}")
    print(f"Total ganho com as vendas: R${totalFeijao + totalArroz + totalFarinha:.2f}")

    confirmacao = str(input("Deseja continuar o programa? (S/N) ")).upper()

print("Programa encerrado.")