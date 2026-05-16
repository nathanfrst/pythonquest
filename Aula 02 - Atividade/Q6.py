while True: 
    print("Bem vindo, qual opção deseja? (1-4) ")
    print("1 - Cadastro de alunos")
    print("2 - Cadastro de Professores")
    print("3 - Setor financeiro")
    print("4 - Sair do programa")
    try:
        menuEscolha = int(input("Digite a opção desejada:"))
    except ValueError:
        print("Entrada inválida. Por favor, digite um número. \n")
        continue

    match menuEscolha:

        case 1:
            print("Cadastro de alunos selecionado.")

            while True:
                nomeAluno = str(input("Digite o nome do aluno: "))
                while True:
                    try:
                        notasAluno1 = float(input("Digite a nota 1 do aluno: "))
                        break
                    except ValueError:
                        print("Entrada inválida. Por favor, digite um número.")
                while True:
                    try:
                        notasAluno2 = float(input("Digite a nota 2 do aluno: "))
                        break
                    except ValueError:
                        print("Entrada inválida. Por favor, digite um número.")

                mediaAluno = (notasAluno1 + notasAluno2) / 2
                if mediaAluno >= 70:
                    print(f"O aluno {nomeAluno} foi aprovado com média {mediaAluno:.2f}")

                elif mediaAluno <= 60 and mediaAluno >= 40:
                    print(f"O aluno {nomeAluno} ficou de recuperação com média {mediaAluno:.2f}")
                else:
                    print(f"O aluno {nomeAluno} foi reprovado com média {mediaAluno:.2f}")

                confAluno = str(input("Deseja cadastrar outro aluno? (S/N) ")).upper()
                if confAluno == "N":
                    break

        case 2:
            print("Cadastro de professores selecionado.")

            nomeProfessor = str(input("Digite o nome do professor: "))
            titulacaoProfessor = str(input("Digite a titulação do professor: ")).upper()
            
            if titulacaoProfessor == "DOUTORADO" or titulacaoProfessor == "MESTRADO":
                print(f"O professor {nomeProfessor} pode orientar projetos.")
            elif titulacaoProfessor == "GRADUAÇÃO":
                print(f"O professor {nomeProfessor} pode administrar aulas básicas.")
            else:
                print("Titulação inválida, programa encerrado.")

        case 3:
            print("Setor financeiro selecionado.")
            usuarioFinanceiro = str(input("Digite qual menu deseja acessar (ALUNO / PROFESSOR): ")).upper()

            if usuarioFinanceiro == "ALUNO":
                valorMensalidade = 1537.59
                mensalidadeDesconto = str(input(f"O valor da mensalidade é: R${valorMensalidade:.2f} você possui algum desconto? (S/N) ")).upper()

                if mensalidadeDesconto == "S":
                    valorDesconto = str(input("Digite o tipo de desconto (BOLSA / PROMOÇÃO): ")).upper()
                    if valorDesconto == "BOLSA":
                        print(f"O valor a ser pago é: R${valorMensalidade:.2f} com desconto de 50%: R${valorMensalidade * 0.5:.2f}")
                        formaPagamento = str(input("Digite a forma de pagamento (DINHEIRO / CARTÃO): ")).upper()

                        if formaPagamento == "DINHEIRO":
                            print(f"O valor a ser pago é: R${valorMensalidade:.2f} com desconto de 10%: R${valorMensalidade * 0.9:.2f}")
                            pagamentoDinheiro = float(input("Insira o valor do pagamento: "))
                            if pagamentoDinheiro >= valorMensalidade * 0.9:
                                print("Pagamento efetuado com sucesso.")
                            else:
                                print("Valor insuficiente, programa encerrado.")

                        elif formaPagamento == "CARTÃO":
                            parcelas =int(input(f"Deseja parcelar em quantas vezes? (1-12) "))
                            if parcelas >= 1 and parcelas <= 12:
                                print(f"O valor a ser pago é: R${valorMensalidade:.2f} em {parcelas}x de R${(valorMensalidade * 1.05) / parcelas:.2f} sem juros")
                                pagamentoParcela = float(input("Insira o valor da primeira parcela:"))
                            if pagamentoParcela >= (valorMensalidade * 1.05) / parcelas:
                                print("Primeira parcela paga com sucesso.")
                            else:
                                print("Valor da parcela insuficiente, programa encerrado.") 

                        else:
                            print("Forma de pagamento inválida, programa encerrado.")

                    elif valorDesconto == "PROMOÇÃO":
                        print(f"O valor a ser pago é: R${valorMensalidade:.2f} com desconto de 25%: R${valorMensalidade * 0.75:.2f}")
                        formaPagamento = str(input("Digite a forma de pagamento (DINHEIRO / CARTÃO): ")).upper()

                        if formaPagamento == "DINHEIRO":
                            print(f"O valor a ser pago é: R${valorMensalidade:.2f} com desconto de 10%: R${valorMensalidade * 0.9:.2f}")
                            pagamentoDinheiro = float(input("Insira o valor do pagamento: "))
                            if pagamentoDinheiro >= valorMensalidade * 0.9:
                                print("Pagamento efetuado com sucesso.")
                            else:
                                print("Valor insuficiente, programa encerrado.")

                        elif formaPagamento == "CARTÃO":
                            parcelas =int(input(f"Deseja parcelar em quantas vezes? (1-12) "))
                            if parcelas >= 1 and parcelas <= 12:
                                print(f"O valor a ser pago é: R${valorMensalidade:.2f} em {parcelas}x de R${(valorMensalidade * 1.05) / parcelas:.2f} sem juros")
                                pagamentoParcela = float(input("Insira o valor da primeira parcela:"))
                            if pagamentoParcela >= (valorMensalidade * 1.05) / parcelas:
                                print("Primeira parcela paga com sucesso.")
                            else:
                                print("Valor da parcela insuficiente, programa encerrado.")
                        else:
                            print("Forma de pagamento inválida, programa encerrado.")
                    else:
                        print("Tipo de desconto inválido, programa encerrado.")

                elif mensalidadeDesconto == "N":
                    print(f"O valor a ser pago é: R${valorMensalidade:.2f}") 
                    formaPagamento = str(input("Digite a forma de pagamento (DINHEIRO / CARTÃO): ")).upper()

                    if formaPagamento == "DINHEIRO":
                        print(f"O valor a ser pago é: R${valorMensalidade:.2f} com desconto de 10%: R${valorMensalidade * 0.9:.2f}")
                        pagamentoDinheiro = float(input("Insira o valor do pagamento: "))
                        if pagamentoDinheiro >= valorMensalidade * 0.9:
                            print("Pagamento efetuado com sucesso.")
                        else:
                            print("Valor insuficiente, programa encerrado.")

                    elif formaPagamento == "CARTÃO":
                        parcelas =int(input(f"Deseja parcelar em quantas vezes? (1-12) "))
                        if parcelas >= 1 and parcelas <= 12:
                            print(f"O valor a ser pago é: R${valorMensalidade:.2f} em {parcelas}x de R${(valorMensalidade * 1.05) / parcelas:.2f} sem juros")
                            pagamentoParcela = float(input("Insira o valor da primeira parcela:"))
                            if pagamentoParcela >= (valorMensalidade * 1.05) / parcelas:
                                print("Primeira parcela paga com sucesso.")
                            else:
                                print("Valor da parcela insuficiente, programa encerrado.")

            elif usuarioFinanceiro == "PROFESSOR":
                horasExtra = int(input("Digite a quantidade de horas extras trabalhadas: "))

                valorSalario = 5560.00
                salarioHora = valorSalario / 160
                valor_horaExtra = (salarioHora * 1.5) * horasExtra
                salarioTotal = valorSalario + valor_horaExtra

                print(f"O valor do salário é: R${valorSalario:.2f}")
                print(f"O valor da hora normal é: R${salarioHora:.2f}")
                print(f"O valor das horas extras é: R${valor_horaExtra:.2f}")
                print(f"O valor total do salário é: R${salarioTotal:.2f}")

            else:
                print("Opção inválida, programa encerrado.")

        case 4:
            print("Programa encerrado.")
        case _:
            print("Opção inválida, programa encerrado.")