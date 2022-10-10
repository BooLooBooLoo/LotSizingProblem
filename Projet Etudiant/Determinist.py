import docplex
from docplex.mp.model import Model
import random
def main(t):
    #On définit le modèle
    m=Model(name='Deterministic')
    m.parameters.mip.tolerances.integrality=1e-15
    #On définit les 2 listes de variables
    x=m.integer_var_list(t,name='x')
    y=m.binary_var_list(t,name='y')
    #On définit les constantes
    #Coût de stockage
    h=[]
    #Demande
    d=[]
    #Coût fixe de production.
    f=[]
    #Capacité de production
    c=[]
    #On définit aléatoirement les constantes
    for i in range(t):
        h.append(random.randint(10,20))
        d.append(random.randint(100,150))
        f.append(random.randint(2000,3000))
        c.append(random.randint(160,200))
    #On définit les contraintes
    for i in range(t):
        #Premiere contrainte, on ne peut pas produire plus que la capacité
        m.add_constraint(x[i]<=c[i]*y[i])
        #Deuxième contrainte, on ne produit pas de choses négatives
        m.add_constraint(x[i]>=0)
        #Troisième contrainte, on ne stocke pas de choses négatives et on respecte la demande
        m.add_constraint(m.sum(x[j] for j in range(i))>=m.sum(d[j] for j in range(i)))
    #On définit la fonction objectif
    m.minimize(m.sum(f[i]*y[i] for i in range(t))+m.sum(h[i]*(m.sum(x[j] for j in range(i))-m.sum(d[j] for j in range(i)))for i in range(t)))
    #On résout le problème
    m.solve()
    #On affiche les résultats
    m.print_information()   
    m.print_solution()
    print(h,"\n",d,"\n",f,"\n",c,"\n")
    print("x=",m.solution.get_values(x))
    print("y=",m.solution.get_values(y))
main(100)
