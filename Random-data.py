import matplotlib.pyplot as plt
from math import pi, cos, sin
from random import random
from random import seed

seed(1)
# 1D Random Number Between [3,7]
a=3
b=7
i=0
print("\nPrint 1D Random Numbers")
for i in range(100):
    print("[",a + (b-a) * random(),"]")

# 2D Random Number Between [3,7] and [2,6] 
a = 3
b = 7
c = 2
d = 6
i = 0
print("\nPrint 2D Random Numbers")
for i in range(100):
    print("[",a + (b-a) * random(),"],[",c+ (d-c)* random(),"]")

# Generating random points on the circumference of a circle
def point(h, k, r):
    theta = random() * 2 * pi
    return h + cos(theta) * r, k + sin(theta) * r


xy = [point(1, 2, 1) for _ in range(30)]
print(xy)

# Show Points
plt.scatter(*zip(*xy))
plt.grid(color='k', linestyle=':', linewidth=1)
plt.axes().set_aspect('equal', 'datalim')
plt.show()
