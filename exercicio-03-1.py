contador=0
situacao=""
maior=0
total=0
menor=1000000
media=0
lista=[]
lista=[6.0,4.3,9.1,3,7.2]
dicionario={}

for i in lista:
    contador=contador+1
    if(i<menor):
        menor=i
    if(i>maior):
        maior=i
    total=total+i
media=total/contador
if(media<7):
    situacao="Ruim"
elif(media<9):
    situacao="Boa"
else:
    situacao="Otima"
print(contador,maior,menor)

dicionario['Quantidade de notas']=contador
dicionario['Maior Nota']=maior
dicionario['Menor Nota']=menor
dicionario['Situação']=situacao
dicionario['Media']=media
print(dicionario)