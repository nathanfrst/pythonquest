
def media():
def aprovados():
def reprovados():

while True:
    try:
        opcao = int(input("Bem vindo ao menu de opções! Digite o número correspondente à opção desejada:\n1. Opção 1\n2. Opção 2\n3. Opção 3\n4. Sair\n"))

        match opcao:
            case 1:

            case 2:
            
            case 3:

            case 4:
                print("Saindo do programa.")
                break
            case _:
                print("Opção inválida. Por favor, escolha uma opção válida.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número correspondente à opção desejada.")