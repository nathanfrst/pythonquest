entregas = int(input("Digite o número de entregas realizadas: "))
totalEntregas = 0

while entregas != 0:
    totalEntregas += entregas
    entregas = int(input("Digite o número de entregas realizadas (Digite 0 para encerrar): "))

print(f"O número total de entregas realizadas é: {totalEntregas}")