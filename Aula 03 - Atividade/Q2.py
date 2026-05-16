produtos = []
def controle_estoque():
        nomeProduto = input("Digite o nome do produto:")
        if nomeProduto in produtos:
            print("Produto já cadastrado.")
        else:
            produtos.append(nomeProduto)
            print("Produto cadastrado com sucesso.")
        confirmacaoCadastro = input("Deseja cadastrar outro produto? (s/n): ")
        if confirmacaoCadastro.lower() == 's':
            controle_estoque()
        elif confirmacaoCadastro.lower() == 'n':
            print("Programa encerrado.")
        else:            
            print("Opção inválida. Por favor, digite 's' para sim ou 'n' para não.")

def listar_produtos():
    if len(produtos) == 0:
        print("Nenhum produto cadastrado.")
    else:
        print("Produtos cadastrados:")
        for produto in produtos:
            print(f"- {produto}")


while True:
    try:
        opcao = int(input("Bem vindo, escolha uma opção: \n1 - Cadastrar produto\n2 - Listar produtos\n3 - Sair\n"))

        match opcao:
            case 1:
                controle_estoque()
            case 2:
                listar_produtos()
            case 3:
                print("Programa encerrado.")
                break
            case _:
                print("Opção inválida. Por favor, escolha uma opção válida.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número correspondente à opção desejada.")


