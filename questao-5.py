print ("Questão 5")
print("")
A = eval(input("Digite a quantidade de habitantes do país A: ")) 
B = eval(input("Digite a quantidade de habitantes do país B: "))
anos = 0
TcrA = eval(input("Digite a taxa de crescimeto anual do país A: (%) "))
TcrB = eval(input("Digite a taxa de crescimeto anual do país B: (%)"))
TcrA = TcrA/100
TcrB = TcrB/100
while (A < B):
                print("País A: ", A, "e País B: ", B, "em",anos,"anos.")
                A = A + (A * TcrA)
                B = B + (B * TcrB)
                anos = anos + 1
    
print("País A em", anos, "anos conseguiu obter uma população maior que o país B." )
print("País A: ", A)
print("País B: ", B)


