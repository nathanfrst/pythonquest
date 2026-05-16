viagensRealizada = 0
entregasFeitas = 0
totalEntregas = 0

while True:
    viagensRealizada = int(input("Digite a quantidade de viagens realizadas:"))
    for entregasFeitas in range(viagensRealizada):
        entregasFeitas = int(input("Digite a quantidade de entregas feitas em cada viagem de maneira respectiva:"))
        totalEntregas += entregasFeitas

    mediaEntregas = totalEntregas / viagensRealizada
    print(f"A média de entregas por viagem é: {mediaEntregas}")