lista_Alunos={}
nome=""
nota1=0
nota2=0
media=0
decisao=1

def Processos(decisao):
    nome=""
    contador=0
    if(decisao==1):
        print(lista_Alunos)
    else:
        nome=input("Insira o nome do aluno\n")
        try:
            print(lista_Alunos[nome])
        except KeyError:
            print("Nome invalido")
            

def Confirmacao(texto):
    refazer=0
    while(refazer==0):
        try:
            try:
                escolha=int(input(texto))
            except ValueError:
                print("O numero foi invalido, tente novamente\n")
        except UnboundLocalError:
            print("O numero foi invalido, tente novamente\n")
        try:
            if(escolha==1):
                escolha=1
            else:
                escolha=2
            return escolha
        except UnboundLocalError:
            escolha=1

def Nota(texto):
    contador=0
    while(contador==0):
        try:
            try:
                numero=float(input(texto+"\n"))
            except ValueError:
                print("O numero foi invalido, tente novamente\n")
        except UnboundLocalError:
            print("O numero foi invalido, tente novamente\n")
        try:
            if((numero>=0)and(numero<=10)):
                contador=1
            return numero
        except UnboundLocalError:
            numero=0

while(decisao==1):
    nome=input("Insira o nome do aluno\n")
    nota1=Nota("Insira a primeira nota")
    nota2=Nota("Insira a segunda nota")
    media=(nota1+nota2)/2
    lista_Alunos[nome]=media
    decisao=Confirmacao("Quer adicionar outro aluno? \n1-Sim\n2-Não\n")

decisao=0
decisao=Confirmacao("Quer fazer qual processo\n1-Ver a lista de todos os alunos\n2-Buscar por aluno especifico\n")
Processos(decisao)
    