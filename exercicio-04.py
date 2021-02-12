teste=0
notas_c=0
notas_v=0
notas_d=0
notas_u=0
def Teste_Numero():
    contador=0
    numero=0
    while(contador==0):
        try:
            try:
                numero=int(input("Insira uma quantidade a ser sacada\n"))
            except ValueError:
                print("O numero foi invalido, tente novamente\n")
        except UnboundLocalError:
            print("O numero foi invalido, tente novamente\n")
        if(numero>0):
            return numero
            contador=1
valor=Teste_Numero()
while(teste==0):
    if(valor>=50):
        valor=valor-50
        notas_c=notas_c+1
    elif(valor>=20):
        valor=valor-20
        notas_v=notas_v+1
    elif(valor>=10):
        valor=valor-10
        notas_d=notas_d+1
    else:
        notas_u=valor
        teste=1
print("{} Notas de cinquenta reais\n{} Notas de vinte reais\n{} Notas de dez reais\n{} Notas de um real".format(notas_c,notas_v,notas_d,notas_u))
