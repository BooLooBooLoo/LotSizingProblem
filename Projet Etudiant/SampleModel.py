import docplex
from docplex.mp.model import Model
import pandas as pd
from random import randint
df = open("random.txt","w")
def Randomizer(T, N):
    for i in range(N):
        for i in range(T):
            rand=randint(20,50)
            df.write(str(rand)+" ")
        df.write('\n')
def ArrayReader():
    #lire le fichier et mettre les valeurs dans un tableau
    df = open("random.txt","r")
    lines = df.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].split()
        for j in range(len(lines[i])):
            lines[i][j] = int(lines[i][j])
    return(lines)
Randomizer(10, 1000)
ArrayReader()
def stochastic(t,N,E):
    #On définit le modèle
    m=Model(name='Deterministic')
    m.parameters.mip.tolerances.integrality=1e-15
    #On définit les 2 listes de variables
    x=m.integer_var_list(t,name='x')
    y=m.binary_var_list(t,name='y')
    a=m.binary_var_list(N,name='a')
    Randomizer(10, 1000)
    array=ArrayReader()
    #calcul de l'espérance pour chaque période
    expectation=[]
    for i in range(t):
        sum=0
        ex=0
        for j in range(N):
            sum+=array[j][i]
            ex=sum/N
        expectation.append(ex)
    h=[]
    #Coût fixe de production.
    f=[]
    #Capacité de production
    c=[]
    #On définit aléatoirement les constantes
    for i in range(t):
        h.append(1)
        f.append(50)
        c.append(100)
    for i in range(t):
        m.add_constraint(x[i]<=c[i]*y[i])
        m.add_constraint(x[i]>=0)
    #sample approximation approach
    for i in range(N):
        for j in range(t):
            m.add_constraint(m.sum(x[k] for k in range(j))>=m.sum(array[i][k] for k in range(j))*(1-a[i]))
    #Contrainte de réussite 
    m.add_constraint(m.sum(a[i] for i in range(N))<=int(N*E))
    #On définit la fonction objectif
    m.minimize(m.sum(f[i]*y[i] for i in range(t))+m.sum(h[i]*(m.sum(x[j] for j in range(i))-m.sum(expectation[j] for j in range(i)))for i in range(t)))
    #On résout le problème
    m.solve()
    #On affiche les résultats
    m.print_information()   
    m.print_solution()
    print(h,"\n",f,"\n",c,"\n")
    print("x=",m.solution.get_values(x))
    print("y=",m.solution.get_values(y))
    print("a=",m.solution.get_values(a))
    sol=0
    xx=m.solution.get_values(x)
    yy=m.solution.get_values(y)
    for i in range(t):
        sol+=f[i]*yy[i]+h[i]*(m.sum(xx[j] for j in range(i))-m.sum(expectation[j] for j in range(i)))
    print("Solution=",sol)
stochastic(10,500,0.05)
    