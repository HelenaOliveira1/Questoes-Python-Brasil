print("Questão 7")
print("")

n1 = eval(input("Digite o primeiro número: "))
n2 = eval(input("Digite o segundo número: "))
n3 = eval(input("Digite o terceiro número: "))
n4 = eval(input("Digite o quarto número: "))
n5 = eval(input("Digite o quinto número: "))

if (n1> n2 and n1> n3 and n1> n4 and n1> n5):
    print("Maior número: ", n1)
elif (n2> n1 and n2> n3 and n2> n4 and n2> n5):
    print("Maior número: ", n2)
elif (n3> n1 and n3> n2 and n3> n4 and n3> n5):
    print("Maior númeor: ", n3)
elif (n4> n2 and n4> n2 and n4> n3 and n4> n5) :
    print("Maior número: ", n4)
elif (n5> n1 and n5> n2 and n5> n3 and n5> n4) :
    print("Maior número: ", n5)
else:
    print("Números Iguais!")
    
