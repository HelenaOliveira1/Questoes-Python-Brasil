print("Questão 3")
print("")
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
salario = float(input("Digite seu salário: "))
sexo = str(input("Digite seu sexo: "))
estado = str(input("Digite seu estado civil: "))

while (len(nome) <= 3):#len é uma função em python que retorna o número de itens da sequência ou coleção
    print("Nome pequeno demais!")
    nome = input("Digite novamente seu nome: ")
    continue
while (idade < 0 or idade > 150):
    print("Idade Inválida")
    idade = int(input("Digite novamente sua idade: "))
    continue
while (salario <= 0):
    print("Inválido")
    salario = float(input("Digite novamente seu salário: "))
    continue
while (sexo != "f" and sexo != "m"):
    print("Seu sexo se refere ao seu orgão genital, portanto você só pode ter sexo Feminino ou Masculino!")
    sexo = str(input("Digite novamente seu sexo: "))
    continue
while (estado != "s" and estado != "c" and estado != "v" and estado != "d"):
    print("Encalhado(a) não é estado civil!")
    print("Estados Civis aceitos: Solteiro(s), Casado(c), Viúvo(v) e Divorciado(d).")
    estado = str(input("Digite novamente seu estado civil: "))
    continue
print("Todas as informações válidas!")
