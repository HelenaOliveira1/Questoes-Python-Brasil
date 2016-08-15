print ("Questão 4")
print("")
#País A - 80000 hab. Taxa de Crescimento anul = 3%
#País B - 200000 hab. Taxa de Crescimento anual = 1.5%
#Taxa de Crescimento anual: A = 0.03 e B = 0.015
#A >= B
#TCA contante
A = 80000
B = 200000
anos = 0
TcrA = 0.03
TcrB = 0.015
while (A < B):
                print("País A: ", A, "e País B: ", B, "em",anos,"anos.")
                A = A + (A * TcrA)
                B = B + (B * TcrB)
                anos = anos + 1
                continue
print("País A em", anos, "anos conseguiu obter uma população maior que o país B." )
print("País A: ", A)
print("País B: ", B)
