preco=0
pagamento=0
parcela=0
def Teste_Numero():
    contador=0
    numero=0
    while(contador==0):
        try:
            try:
                numero=int(input("Insira o preço do produto\n"))
            except ValueError:
                print("O numero foi invalido, tente novamente\n")
        except UnboundLocalError:
            print("O numero foi invalido, tente novamente\n")
        if(numero>0):
            return numero
            contador=1

def Pergunta_int(texto):
    contador=0
    while(contador==0):
        try:
            try:
                numero=int(input(texto+"\n"))
            except ValueError:
                print("O numero foi invalido, tente novamente\n")
        except UnboundLocalError:
            print("O numero foi invalido, tente novamente\n")
        if((numero>=1)and(numero<=4)):
           contador=1
           return numero

def Desconto(preco,pagamento):
    desconto=0
    if(pagamento==1):
        desconto=(preco/100)*50
    if(pagamento==2):
        desconto=(preco/100)*10
    if(pagamento==3):
        desconto=((preco/100)*10)*-1
    if(pagamento==4):
        desconto=((preco/100)*50)*-1
    return desconto

def Parcela(preco,pagamento):
    parlela=0
    if(pagamento==1):
        parcela=preco
    if(pagamento==2):
        parcela=preco
    if(pagamento==3):
        parcela=preco/5
    if(pagamento==4):
        parcela=preco/10
    return parcela

preco=Teste_Numero()
pagamento=Pergunta_int("Escolha sua forma de pagamento\n1-A vista\n2-A prazo sendo 1x no cartão\n3-A prazo da loja em 5x\n4-A prazo da loja em 10x")
desconto=Desconto(preco,pagamento)
preco=preco-desconto
parcela=Parcela(preco,pagamento)

print("O preço do produto original é {}, cada parcela é {}".format(preco,parcela))