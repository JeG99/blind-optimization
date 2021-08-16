
import math
import numpy as np
import pandas as pd

from random import uniform
from utils import ackley
from matplotlib import pyplot as plt

plt.close("all")

experiments = pd.DataFrame()

def generate_solution(min, max, n):
    return [uniform(min, max) for i in range(n)]

def mutate(x_p, delta, min, max):
    x_m = [x + uniform(-delta, delta) for x in x_p]
    valid = True
    for x_i in x_m:
        valid = valid and x_i > min and x_i < max and x_i != 0
    if not valid:
        #print("Bad:", x_m)
        return mutate(x_p, delta, min, max) 
    else:
        #print("Good:", x_m)
        return x_m

def eval(x_i):
    return ackley(x_i, 20, 0.2, 2 * math.pi)

def generate_sons(x_p, n, delta):
    sons = []
    for i in range(n):
        sons.append(mutate(x_p, delta, -32.768, 32.768))
    return sons

# Generar padre inicial
parent = generate_solution(-32.768, 32.768, 2)

print("First parent:", parent)


# Un padre varios hijos
def opms(x_p):
    intentos = 0
    parents = [x_p]
    evaluations = [eval(x_p)]
    #while(sum(x_p) > 1 or sum(x_p) < -1):
    #while(x_p[0] < -1 or x_p[0] > 1 or x_p[1] < -1 or x_p[1] > 1):
    while(intentos < 10):
        # Generar hijos
        sons = generate_sons(x_p, 30, 10)
        
        # Evaluar para selección
        curr_eval = eval(x_p)
        sons_eval = [eval(son) for son in sons]

        # Selección
        print(sons[ sons_eval.index(min(sons_eval)) ])
        if min(sons_eval) < curr_eval:
            x_p = sons[ sons_eval.index(min(sons_eval)) ]
            parents.append(x_p)
            evaluations.append(eval(x_p))
        
        intentos += 1

    parents = np.array(parents)
    experiments['x1'] = parents[:,0]
    experiments['x2'] = parents[:,1]
    experiments['f(x)'] = evaluations
    experiments.plot()
    plt.show()
    
    return x_p

# Varios padres varios hijos
def mpms():
    pass

print(eval([1, 1]))

opms(parent)
print(experiments)
#plt.plot([ackley([x], 20, 0.2, 2 * math.pi) for x in range(-32, 32)])
#plt.show()

