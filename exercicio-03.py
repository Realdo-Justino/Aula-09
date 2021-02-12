numero_Notas_Totais=0
total_Turma=0
media_Turma=0
situacao_Aluno=""
decisao=0
nota=0
n_Notas=0
dicionario=[]

def Dicionario():
    print("oi")

def Pergunta_int(texto):
    numero=0
    while(numero==0):
        try:
            try:
                numero=int(input(texto+"\n"))
            except ValueError:
                print("O numero foi invalido, tente novamente\n")
        except UnboundLocalError:
            print("O numero foi invalido, tente novamente\n")
        if(numero==1):
            numero=1
        elif(numero>1):
            numero=2
        else:
            numero=0
    return numero

def Teste_numero(texto):
    numero=0
    while(numero==0):
        try:
            try:
                numero=int(input(texto+"\n"))
            except ValueError:
                print("O numero foi invalido, tente novamente\n")
        except UnboundLocalError:
            print("O numero foi invalido, tente novamente\n")
        if((numero<10)(numero>0)):
            return numero
        else:
            numero=0

while(decisao==2):
    numero_Notas=0
    maior_Nota=0
    menor_Nota=1000000000000
    while(n_Notas==2):
        numero_Notas=numero_Notas+1
        nota=Teste_numero("Insira sua nota")
        n_Notas=Pergunta_int("Deseja adicionar mais uma nota?\n1-Sim\n2-Não")
    if(maior_Nota<nota):
        maior_Nota=nota
    if(menor_Nota>nota):
        menor_Nota=nota
    total_Turma=total_Turma+nota
    situacao_Aluno=input("Insira a situação do aluno")
    Dicionario(numero_Notas,maior_Nota,menor_Nota)
    numero_Notas_Totais=numero_Notas_Totais+numero_Notas
    decisao=Pergunta_int("Deseja adicionar mais um aluno?\n1-Sim\n2-Não")
media_Turma=total_Turma/numero_Notas_Totais