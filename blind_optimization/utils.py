import math
from random import uniform, randint

def ackley(sol, a, b, c):
    d = len(sol)

    sum_1 = 0
    sum_2 = 0
    for x in sol:
        #if x == 0:
        #    return 
        sum_1 += x * x
        sum_2 += math.cos(c * x)

    try:
        output = -a * math.e ** ( (sum_1/d) ** (-1/b) ) - math.e ** (sum_2/d) + a + math.e
        return output
    except:
        pass

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

def f_eval(x_i):
    return ackley(x_i, 20, 0.2, 2 * math.pi)

def op_generate_children(x_p, n, delta):
    children = []
    for i in range(n):
        children.append(mutate(x_p, delta, -32.768, 32.768))
    return children

def mp_generate_children(x_ps, n, delta):
    children = []
    for i in range(n):
        children.append(mutate(x_ps[ randint(0, len(x_ps)-1) ], delta, -32.768, 32.768))
    return children

