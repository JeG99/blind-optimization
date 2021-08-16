import math

def ackley(sol, a, b, c):
    d = len(sol)

    sum_1 = 0
    sum_2 = 0
    for x in sol:
        #if x == 0:
        #    return 
        sum_1 = sum_1 + x * x
        sum_2 = sum_2 + math.cos(c * x)

    try:
        output = -a * math.e ** ( (sum_1/d) ** (-1/b) ) - math.e ** (sum_2/d) + a + math.e
        return output
    except:
        pass