import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

from utils import f_eval, op_generate_children, mp_generate_children

# Un padre varios hijos
def opmc(x_p, gen_overlap, iter=5, n_children=10):
    iters = pd.DataFrame()
    
    count = 1
    parents = [x_p]
    evaluations = [f_eval(x_p)]

    while(count < iter):
        # Generar hijos
        children = op_generate_children(x_p, n_children)
        if gen_overlap:
            children.append(x_p)
        # Evaluar para selección
        children_eval = [f_eval(child) for child in children]
    
        # Selección
        x_p = children[ np.argmin(children_eval) ]
        count += 1

        parents.append(x_p)
        evaluations.append(f_eval(x_p))
        if gen_overlap:
            children.pop()

    parents = np.array(parents, dtype='object')
    iters['iterations'] = range(0, iter)
    iters['x1'] = parents[:, 0]
    iters['x2'] = parents[:, 1]
    iters['f(x)'] = evaluations
    
    #plt.figure()
    #plt.plot(iters.index, iters['x1'])
    #plt.plot(iters.index, iters['x2'])
    #plt.show()

    return x_p, iters

# Varios padres varios hijos
def mpmc(x_p, gen_overlap, iter=5, n_children=10):
    iters = pd.DataFrame()
    
    count = 1
    
    evs = [f_eval(x_i) for x_i in x_p]
    evaluations = [min( evs )]
    parents = [ x_p[evs.index(evaluations[0])] ]

    while(count < iter):
        # Generar hijos
        children = mp_generate_children(x_p, n_children)
        
        if gen_overlap:
            children += x_p
        # Evaluar para selección
        children_eval = [f_eval(child) for child in children]

        # Selección
        #try:
        for i in range(len(x_p) - 1):
            x_p[i] = children[ np.argmin(children_eval) ]
            #x_p[i] = children[ children_eval.index(min(children_eval)) ]
            children.pop( np.argmin(children_eval) )
            children_eval.pop( np.argmin(children_eval) )
        count += 1
        #except TypeError:
        #    continue

        parents.append(x_p[0])
        evaluations.append(f_eval(x_p[0]))

    parents = np.array(parents, dtype='object')
    iters['iterations'] = range(0, iter)
    iters['x1'] = parents[:, 0]
    iters['x2'] = parents[:, 1]
    iters['f(x)'] = evaluations
    
    #plt.figure()
    #plt.plot(iters.index, iters['x1'])
    #plt.plot(iters.index, iters['x2'])
    #plt.show()

    return x_p[0], iters
