from cmath import log
import docplex
from docplex.mp.model import Model
import math

def objective(t, E, dmin, dmax):
    #On définit le modèle
    m = Model(name="MS1Model")
    m.parameters.mip.tolerances.integrality=1e-20

    #On définit les constantes
    jVal = dmax - dmin
    F = []
    for i in range(dmin, dmax+1):
        F.append((i-dmin+1)/(jVal+1))
    #On définit les listes de variables
    x = m.integer_var_list(t,name='x')
    y = m.binary_var_list(t,name='y')
    z = {k: m.binary_var_list(jVal+1, name="w_{0}".format(k)) for k in range(t)}
    w = m.integer_var_list(t,name='w')
    I = m.integer_var_list(t+1, name='I')

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

    #On définit les contraintes
    for i in range(t):
        m.add_constraint(x[i]<=c[i]*y[i])
        m.add_constraint(x[i]>=0)
        m.add_constraint(I[0] == 0)
        m.add_constraint(m.sum(z[i][k] for k in range(1,jVal+1)) == 1)
        m.add_constraint(w[i] == m.sum(j*z[i][j-dmin] for j in range(dmin,dmax+1)))
        m.add_constraint(I[i] >= 0)
        m.add_constraint(I[i] + x[i] - I[i+1] >= w[i])
        m.add_constraint(m.sum(m.sum(z[i][k]*math.log(F[k]) for k in range(jVal+1))) >= math.log(1-E))

    #On définit la fonction objectif
    m.minimize(m.sum(f[i]*y[i] for i in range(t))+m.sum(h[i]*I[i] for i in range(t)))
    m.solve()

    #On affiche les résultats
    print("Solution status: ", m.solve_details.status)
    print("Solution value: ", m.objective_value)
    print("Solution: ")
    for i in range(t):
        print("x[",i,"] = ", x[i].solution_value)
        print("y[",i,"] = ", y[i].solution_value)
        print("w[",i,"] = ", w[i].solution_value)
        print("I[",i,"] = ", I[i].solution_value)
        for k in range(jVal):
            if z[i][k].solution_value == 1:
                print("z[",i,",",k,"] = ", z[i][k].solution_value)

objective(10, 0.05, 20, 50)

    
