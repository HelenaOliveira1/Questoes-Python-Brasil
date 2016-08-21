print("Questão 8")
print("")

quant = 5
print("")

i = 0
soma = 0

while (i < quant):
    num = int(input("Informe o número: "))
    soma += num
    i += 1
    continue

media = soma/quant
print("")
print("A média dos números é: ", media)
