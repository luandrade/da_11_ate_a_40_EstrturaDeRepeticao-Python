quantidade_cd=int(input("-informe a quantidade de CDs adiquiridos: \n "))
somador=0
for c in range(1,quantidade_cd+1):
    pre�o=float(input("-informe o pre�o de cada CD--> "))
    somador=somador + pre�o
    media=somador/quantidade_cd
print("-total investido =",somador,"$")
print("-valor gasto em cada CD =",media,"$")