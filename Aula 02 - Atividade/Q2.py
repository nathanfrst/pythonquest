loginRegist = str(input("Digite o email a ser registrado: "))
senhaRegist = str(input("Digite a senha a ser registrada: "))

login = str(input("Digite seu email: "))
senha = str(input("Digite sua senha: "))

while login != loginRegist or senha != senhaRegist:
    print("Email ou senha incorretos, tente novamente.")
    login = str(input("Digite novamente seu email: "))
    senha = str(input("Digite novamente sua senha: "))

print("Login realizado com sucesso!")
