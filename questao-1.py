#Programa para avaliar a turma 1°B informática
print("Exercício Estrutura de Repetição")
print("")
print("Questão 1")
print("")
nota = float(input("Que nota merecemos? (Por favor de 0 a 10)"))

while (nota < 0 or nota > 10):
	print("Nota inválida!")
	print("")
	nota = float(input("Que nota merecemos? (Por favor de 0 a 10)"))
	continue

if (nota == 10):
        print("Muito Obrigado =)")
else:
    print("")
    print("Obrigado!")
