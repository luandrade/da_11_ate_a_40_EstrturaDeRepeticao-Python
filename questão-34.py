#Os n�meros primos possuem v�rias aplica��es dentro da Computa��o, por exemplo na Criptografia. Um n�mero primo � aquele que � divis�vel apenas por um e por ele mesmo. Fa�a um programa que pe�a um n�mero inteiro e determine se ele � ou n�o um n�mero primo
num=int(input("-Digite Um Numero--> "))        
contaresto=0        
for c in range(1,num+1):        
    resto=num%c    
    if resto==0:        
        contaresto=contaresto+1    
if contaresto==1 or contaresto==2:
    print(num,"� primo")
else:
    print(num,"nao � primo")