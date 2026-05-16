itensTotal = 0
itensLote = 0

while True:
    lotesDiario = int(input("Digite a quantidade de lotes recebidos: "))
    for itensLote in range(lotesDiario):
        itensLote = int(input("Digite a quantidade de itens presente em cada lote:"))
        itensTotal += itensLote
    
    print(f"O valor total de itens recebidos é: {itensTotal} itens.")