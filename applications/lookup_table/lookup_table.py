import math
import random
d = {}
def slowfun(x, y):
    
    # TODO: Modify to produce the same results, but much faster
    if (x, y) not in d:
        v = math.pow(x, y)
        v = math.factorial(v)
        v //= (x + y)
        v %= 982451653
        d[(x,y)] = v
    return d[(x,y)]
    


# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
