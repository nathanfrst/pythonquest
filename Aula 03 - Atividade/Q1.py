clientes = []
def cadastro_clientes():
    while True:
        try: 
            nome = input("Digite o nome do cliente:")
            if nome in clientes:
                print(f"Cliente {nome} já cadastrado.")
                continue
            elif nome not in clientes:
                clientes.append(nome)
                print(f"Cliente {nome} cadastrado com sucesso.")
            retornar = input("Deseja cadastrar outro cliente? (S/N):").upper()

            if retornar == "N":
                break
            elif retornar != "S":
                print("Opção inválida. Retornando ao menu principal.")
                break
            
        except ValueError:
            print("Ocorreu um erro. Tente novamente.")

def remover_cliente():
    nomeRemover = input("Digite o nome do cliente a ser removido:")
    if nomeRemover in clientes:
        clientes.remove(nomeRemover)
        print(f"Cliente {nomeRemover} removido com sucesso.")
    else:
        print(f"Cliente {nomeRemover} não encontrado.")

def listar_clientes():
    for cliente in clientes:
        print(f"Clientes cadastrados no sistema: {cliente}")


while True:
    try:
        print("Bem vindo ao sistema de cadastro de clientes. \n")
        print("1 - Cadastrar cliente \n2 - Remover cliente \n3 - Listar clientes \n4 - Sair")

        opcaoMenu = int(input("Digite a opção desejada:"))

        match opcaoMenu:
            case 1:
                cadastro_clientes()
            case 2:
                remover_cliente()
            case 3:
                listar_clientes()
            case 4:
                print("Saindo do sistema...")
                break
            case _:
                print("Opção inválida. Tente novamente.")
        
    except ValueError:
        print("Ocorreu um erro. Tente novamente.")

