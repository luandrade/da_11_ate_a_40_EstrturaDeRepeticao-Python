quantidade=int(input("quantidade de produtos comprados--> "))
soma=0
for produtos in range (1,quantidade+1):
    pre�o=float(input("informe o pre�o dos produtos--> "))
    soma=soma+pre�o
    
print("total = R$",soma)
dinheiro=float(input("dinheiro total--> "))
troco=dinheiro-soma
print("troco: R$",troco)