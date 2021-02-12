refazer=0
while(refazer==0):
    from random import seed
    from random import randint
    seed(1)
    escolha=0
    valor=0
    def Jogo(escolha,valor):
        if(escolha==valor):
            print("Empate")
        elif((escolha-1<0)and(valor==3)):
            print("Voce perdeu")
        elif(escolha+1==valor):
            print("Voce venceu")
        else:
            print("Voce perdeu")
    def Teste_Numero(escolha):
        while(escolha==0):
            try:
                try:
                    escolha=int(input("Escolha 1\n1-Papel\n2-Pedra\n3-Tesoura\n"))
                except ValueError:
                    print("O numero foi invalido, tente novamente\n")
            except UnboundLocalError:
                print("O numero foi invalido, tente novamente\n")
            if((escolha<0)or(escolha>3)):
                print("Por favor escolha uma opção valida\n")
                escolha=0
            else:
                return escolha

    escolha=Teste_Numero(escolha)
    valor2=randint(1,2132)
    for i in range(valor2):
        valor=randint(1,3)
    print(valor)
    Jogo(escolha,valor)
    try:
        try:
            escolha=int(input("Quer jogar denovo \n1-sim\n2-Não\n"))
        except ValueError:
            print("O numero foi invalido, tente novamente\n")
    except UnboundLocalError:
        print("O numero foi invalido, tente novamente\n")
    if(escolha==1):
        refazer=0
    else:
        refazer=1
    