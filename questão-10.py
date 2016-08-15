print("Questão 10")
print("")

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
for result in range(n1+1, n2):
    print(result)
for result in range (n2+1, n1):
    print(result)
