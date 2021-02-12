numero=0
texto=""
conta=0
def Teste_Numero(numero):
    while(numero==0):
        try:
            try:
                numero=int(input("Insira um numero de 1 a 10\n"))
            except ValueError:
                print("O numero foi invalido, tente novamente\n")
        except UnboundLocalError:
            print("O numero foi invalido, tente novamente\n")
        if((numero<0)or(numero>10)):
            print("O numero precisa ser entre 1 e 10\n")
            numero=0
        else:
            return numero

numero=Teste_Numero(numero)
print("\n")
for i in range(1,11):
    conta=numero*i
    texto+="{}x{}={}\n".format(numero, i, conta)
print(texto)