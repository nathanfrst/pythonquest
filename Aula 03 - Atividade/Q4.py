folhaSalarial = []   
def cadastrarFuncionario():
    nome = input("Digite o nome do funcionário: ")
    salario = float(input("Digite o salário do funcionário: "))

    funcionarios = [nome, salario]
    folhaSalarial.append(funcionarios)

while True: 
    try:
        opcao = int(input("Bem vindo, escolha uma opção: \n1 - Cadastrar funcionário\n2 - Listar folha salarial e classe\n3 - Sair\n"))
        
        match opcao:
            case 1:
                cadastrarFuncionario()
            case 2:
                for funcionario in folhaSalarial:
                    nome = funcionario[0]
                    salario = funcionario[1]

                    if salario <= 2500:
                        print(f"Funcionário: {nome} - Salário: {salario}R$ - Classe: E")
                    elif salario > 2500 and salario <= 7000:
                        print(f"Funcionário: {nome} - Salário: {salario}R$ - Classe: D")
                    elif salario > 7000:
                        print(f"Funcionário: {nome} - Salário: {salario}R$ - Classe: C")
                    else:
                        print("Salário inválido. Por favor, digite um valor válido.")

            case 3:
                print("Programa encerrado.")
                break
            case _:
                print("Opção inválida. Por favor, escolha uma opção válida.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número correspondente à opção desejada.")