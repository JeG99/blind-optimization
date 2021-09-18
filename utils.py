import math
import numpy as np
from random import uniform, randint

def ackley(sol, a, b, c):
    d = len(sol)

    sum_1 = 0
    sum_2 = 0
    for x in sol:
        sum_1 += x * x
        sum_2 += math.cos(c * x)

    try:
        output = -a * math.e ** ( (math.sqrt(sum_1/d)) * (-b) ) - math.e ** (sum_2/d) + a + math.e
        return output
    except:
        pass

def generate_solution(min, max, n):
    return [uniform(min, max) for i in range(n)]

def mutate(x_p, min, max):
    x1 = x_p[0] + (-1) ** np.random.randint(0, 2) * np.random.random_sample(size=1)
    x2 = x_p[1] + (-1) ** np.random.randint(0, 2) * np.random.random_sample(size=1)
    return [np.clip(x1, min, max), np.clip(x2, min, max)]

def f_eval(x_i):
    return ackley(x_i, 20, 0.2, 2 * math.pi)

def op_generate_children(x_p, n):
    children = []
    for i in range(n):
        children.append(mutate(x_p, -32.768, 32.768))
    return children

def mp_generate_children(x_ps, n):
    children = []
    for i in range(n):
        children.append(mutate(x_ps[ randint(0, len(x_ps)-1) ], -32.768, 32.768))
    return children

