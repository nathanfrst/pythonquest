valorTotal = 0
    
while True:
    comprasDiario = int(input("Digite a quantidade de compras: "))
    for valorCompra in range(comprasDiario):
        valorCompra = float(input("Digite o valor das compras de maneira respectiva: "))
        valorTotal += valorCompra
    print(f"O valor total das compras é: R${valorTotal:.2f}")

    break