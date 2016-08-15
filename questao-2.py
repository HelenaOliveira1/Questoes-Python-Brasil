print("Questão 2")
print("")
nome = input("Digite seu nome: ")
senha = input("Digite sua senha: ")
while (senha == nome):
        print("INVÁLIDO!")
        print("Nome e Senha não podem ser iguais!")
        print("")
        nome = str(input("Digite seu nome: "))
        senha = eval(input("Digite sua senha: "))
        continue
print("Obrigado!")
