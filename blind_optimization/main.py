
import math
import numpy as np
import pandas as pd

from utils import generate_solution as generate_solution
from parent_children import opmc, mpmc
from matplotlib import pyplot as plt

plt.close("all")

def poner_menor(row):
    df.at[row.name, 'menor'] = min(row['evaluacion'], df.iloc[row.name - 1].menor)
    return None

# Generar padre inicial
df_experiments = pd.DataFrame()
best_parents = []
experiments = []

for i in range(5):
    #parent = generate_solution(-32.768, 32.768, 2)
    #best_parent, iterations = opmc(parent, False, 1000, 100)

    parents = [generate_solution(-32.768, 32.768, 2) for i in range(10)]
    best_parent, iterations = mpmc(parents, True, 100, 100)

    best_parents.append(best_parent)
    experiments.append(iterations)
    cantidad = len(iterations)
    df = pd.DataFrame(
        {'algoritmo':["UnPadreVariosHijos"] * cantidad,
         'experimento':[i]*cantidad,
         'iteracion':list(range(0, cantidad)),
         'x1':iterations['x1'],
         'x2':iterations['x2'],
         'evaluacion':iterations['f(x)']}
    )
    df.at[0, 'menor'] = df.loc[0]['evaluacion']

    df.loc[1:].apply(lambda row: poner_menor(row), axis=1)

    print(df)

    df_experiments = df_experiments.append(df)

df_experiments.reset_index(drop=True, inplace=True)
results = df_experiments.groupby('iteracion').agg({'menor': ['mean', 'std']})
print(results)
# print(best_parents)
#results.plot()

promedios = results['menor']['mean'].values
std = results['menor']['std'].values
plt.plot(range(0,cantidad), promedios, color='red', marker='*')
plt.plot(range(0,cantidad), promedios+std, color='b', linestyle='-.')
plt.plot(range(0,cantidad), promedios-std, color='b', marker='o')
plt.xlabel('iteraciones')
plt.ylabel('menor encontrado')
plt.legend(['promedio', 'promedio+std','promedio-std'])
plt.title('1P-VH')
plt.show()



