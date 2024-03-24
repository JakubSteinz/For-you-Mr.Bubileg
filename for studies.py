import math
def S(r):
    return round(math.pi * r**2, 2)
print(S(5))

def O(r):
    return round(math.pi * 2 * r, 3)
print(O(5))

x = 0.01
for i in range (30):
    x = x * 2
    print(x)
