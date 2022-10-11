import docplex
from docplex.mp.model import Model
import pandas as pd
from random import randint

df = open("random.txt","w")
def Randomizer(T, N, dmin, dmax):
    for i in range(N):
        for i in range(T):
            rand=randint(dmin,dmax)
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

def objective(t, dmin, dmax):
    #On définit le modèle
    m = Model(name="MS1Model")
    m.parameters.mip.tolerances.integrality=1e-15

    #On définit les constantes
    j = dmax - dmin

    #On définit les listes de variables
    x=m.integer_var_list(t,name='x')
    y=m.binary_var_list(t,name='y')
    z=m.binary_var_matrix(t, j,name='z')
    w=m.integer_var_list(t,name='w')
    I = m.integer_var_list(t, name='I')
    #On appelle le randomizer
    Randomizer(10, 1000, dmin, dmax)
    ArrayReader()

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
