quantidade=int(input("quantidade de temperaturas--> "))
temperaturas=int(input("informe as temperaturas--> "))
menor=temperaturas
maior=temperaturas
somador=temperaturas
for i in range(1,quantidade):
    temperaturas=float(input("informe as temperaturas--> "))
    somador=somador+temperaturas
    if temperaturas>maior:
        maior=temperaturas
    elif temperaturas<menor:
        menor=temperaturas
print("o maior �", maior)
print("o menor �",menor)
print("a media das temperaturas �-->",somador/quantidade)