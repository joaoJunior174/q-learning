import sys
import random
#retorna o maximo elemento na matriz (argmax)
def pegaMax(estadoFinal,mat):
   min = -100
   if (estadoFinal == 5):
      return 0


   for i in range(7):
      if(mat[estadoFinal][i] > min):

         min=mat[estadoFinal][i]
   
   return min

#printa a matriz
def printGrid(mat):
    for i in range(1,7):
        print(i,end = '-') 
        for j in range(1,7):
           print ("%.2f" % mat[i][j],end = ' ')
   
        print(" ")
    	

#calcula V e pi
def funcOtima(pi,v,gridWorld):
    for i in range(1,7):
        num=pegaMax(i,gridWorld)
        v[i]=num
        
    for i in range(1,7):
        for j in range(1,7):
           if(gridWorld[i][j] == v[i]):
               pi[i].append(j)

#retira a coluna e valores zero dos vetores V e pi
def formatarSaida(pi,v):
    v.pop(0)
    for i in range(1,7):
      pi[i].pop(0)
    pi.pop(0)
    
#mundo de grades 3x2 modelado em matriz
gridWorld=[[0,0,0,0,0,0,0], 
           [0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0]]
 
it=50;#numero de iteracoes para resolver o problema
gridWorld[6][5]=100#inicia os pesos do objetivo com 100
gridWorld[4][5]=100
#variaveis dadas no exercicio
a=0.1
y=0.9
#estados iniciais
estadoInicial=1
estadoFinal=4
#faz a iteracao para o problema
for i in range(it):
    #chuta um estado aleatorio
    if(estadoInicial==0):
 
           
        estadoInicial = random.randint(1, 6)

        if(estadoInicial==5):
            estadoInicial=1  
        #chuta um estado aleatorio final possivel se o estado aleatorio foi 1
        if(estadoInicial ==1):
            aux=[]
            aux.append(2)
            aux.append(4)
            index = random.randint(0, 1)
            estadoFinal=aux[index]

          #chuta um estado aleatorio final possivel se o estado aleatorio foi 2         
        elif(estadoInicial ==2):
            aux=[]
            aux.append(1)
            aux.append(3)
            index = random.randint(0, 1)
            estadoFinal=aux[index]
       
        elif(estadoInicial ==3):
            aux=[]
            aux.append(2)
            aux.append(4)
            aux.append(6)
            index = random.randint(0, 2)
            estadoFinal=aux[index]
       
    
        elif(estadoInicial == 4):
            aux=[]
            aux.append(1)
            aux.append(3)
            aux.append(5)
            index = random.randint(0, 2)
            estadoFinal=aux[index]
       
        elif(estadoInicial ==6):
            aux=[]
            aux.append(5)
            aux.append(3)
            index = random.randint(0, 1)
            estadoFinal=aux[index]

    #print("Estado inicial: ",estadoInicial," Estado final: ",estadoFinal)
    #formula para o q
    q = (1-a)*gridWorld[estadoInicial][estadoFinal]+a*(gridWorld[estadoInicial][estadoFinal]+y*pegaMax(estadoFinal,gridWorld))   
    #print((1-a)*gridWorld[estadoInicial][estadoFinal])
    #print(gridWorld[estadoInicial][estadoFinal]+y*pegaMax(estadoFinal,gridWorld))
    #atualizo os pesos
    gridWorld[estadoInicial][estadoFinal]=q
    #reinicio os estados
    estadoInicial=0
    estadoFinal=0
#variaveis para o V e valores de Pi
pi=[[0],[0],[0],[0],[0],[0],[0]]
v=[0,0,0,0,0,0,0]

#chamada das funcoes
funcOtima(pi,v,gridWorld)
formatarSaida(pi,v)

#print dos resultados
printGrid(gridWorld)
print(pi)
print(v)

