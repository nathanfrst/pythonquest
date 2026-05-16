def salario_liquido():
    salario_bruto = float(input("Digite o salário bruto:"))
    desconto = float (input("Digite o valor do desconto:"))
    salario_liquido = salario_bruto - (salario_bruto * desconto / 100)
    print(f"O salário líquido é: {salario_liquido}R$")

salario_liquido()