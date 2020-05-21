"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

#q = set(range(1, 10))
#q = set(range(1, 200))
q = (1, 3, 4, 7, 12)
dmin = {}
dsum = {}

def f(x):
    return x * 4 + 6

# TODO: Implement me.
def sum_diff(q):
    for i in q:
        for x in q:
            if (i,x) not in dsum:
                dsum[(i,x)] = f(i) + f(x)
    for i in q:
        for x in q:
            if (i,x) not in dmin:
                dmin[(i,x)] = f(i) - f(x)

    for k, v in dsum.items():
        for mk, mv in dmin.items():
            if v == mv:
                print(f'f({k[0]}) + f({k[1]}) = f({mk[0]}) - f({mk[1]})')    

sum_diff(q)