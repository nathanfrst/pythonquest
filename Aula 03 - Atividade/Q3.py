vendas = []

def cadastrarVendas():
    while True:
        try:
            vendasUser = int(input("Digite o valor das vendas da loja: "))
            vendas.append(vendasUser)
            confirmacaoCadastro = input("Deseja cadastrar outro valor de venda? (s/n): ")
            if confirmacaoCadastro.lower() == 's':
                continue
            else:
                break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número correspondente ao valor das vendas.")

def totalVendas():
    total = sum(vendas)
    return total

def minVendas():
    if vendas:
        return min(vendas)
    else:
        print("Nenhuma venda cadastrada.")
        return None

def maxVendas():
    if vendas:
        return max(vendas)
    else:
        print("Nenhuma venda cadastrada.")
        return None
    
    
while True:
    try:
        print("Bem vindo, escolha uma opção: \n1 - Cadastrar vendas\n2 - Total de vendas\n3 - Valor mínimo de vendas\n4 - Valor máximo de vendas\n5 - Sair")
        opcao = int(input("Digite a opção desejada: "))

        match opcao:
            case 1:
                cadastrarVendas()
            case 2:
                print(f"Total de vendas: {totalVendas()}R$")
            case 3:
                print(f"Valor mínimo das vendas: {minVendas()}R$")
            case 4:
                print(f"Valor máximo das vendas: {maxVendas()}R$")
            case 5:
                print("Programa encerrado.")
                break
            case _:
                print("Opção inválida. Por favor, escolha uma opção válida.")       
        
    except ValueError:
        print("Entrada inválida. Por favor, digite um número correspondente ao valor das vendas.")