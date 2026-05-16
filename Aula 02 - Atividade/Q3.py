comprasCliente = float(input("Digite o valor da compra: "))
somaCompras = 0

while comprasCliente != 0:
    somaCompras += comprasCliente
    comprasCliente = float(input("Digite o valor da compra (Digite 0 para encerrar e ver o total): "))

print(f"O valor total das compras é: {somaCompras}")