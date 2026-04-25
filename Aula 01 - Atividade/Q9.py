genero = input("Digite seu genero (M para Masculino e F para feminino): ").upper()

if genero == 'M':
    altura = float(input("Digite sua altura em cm: "))
    pesoIdeal = 52 + (0.75 * (altura - 152.4))
    print("Seu peso ideal é ", pesoIdeal, " kg")
elif genero == 'F':
    altura = float(input("Digite sua altura em cm: "))
    pesoIdeal = 49 + (0.67 * (altura - 152.4))
    print("Seu peso ideal é ", pesoIdeal, " kg")
else:
    print("Por favor insira um caractere válido ")
