
import math
import numpy as np
import pandas as pd

from random import uniform
from utils import ackley
from matplotlib import pyplot as plt

plt.close("all")

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

def generate_children(x_p, n, delta):
    children = []
    for i in range(n):
        children.append(mutate(x_p, delta, -32.768, 32.768))
    return children

# Generar padre inicial
parent = generate_solution(-32.768, 32.768, 2)

print("First parent:", parent)

# Un padre varios hijos
def opmc(x_p, gen_overlap, iter=5, n_children=10, delta=10):
    iters = pd.DataFrame()
    
    count = 1
    parents = [x_p]
    evaluations = [eval(x_p)]

    while(count < iter):
        # Generar hijos
        children = generate_children(x_p, n_children, delta)
        if gen_overlap:
            children.append(x_p)
        # Evaluar para selección
        curr_eval = eval(x_p)
        children_eval = [eval(child) for child in children]

        # Selección
        try:
            x_p = children[ children_eval.index(min(children_eval)) ]
            count += 1
        except TypeError:
            continue

        parents.append(x_p)
        evaluations.append(eval(x_p))
        if gen_overlap:
            children.pop()

    parents = np.array(parents)
    iters['iterations'] = range(0, iter)
    iters['x1'] = parents[:, 0]
    iters['x2'] = parents[:, 1]
    iters['f(x)'] = evaluations
    
    return x_p, iters

best_parents = []
experiments = []
for i in range(1):
    best_parent, iterations = opms(parent, False, 100, 100, 100)
    best_parents.append(best_parent)
    experiments.append(iterations)

results = pd.concat(experiments, ignore_index=True)
#with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
print(results)
#results.plot()

plt.figure()
plt.plot(results.index, results['x1'])
plt.plot(results.index, results['x2'])
plt.show()



