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

# 2D Random Number Between [3,7] and [] 
a = 3
b = 7
c = 2
d = 6
i = 0
print("\nPrint 2D Random Numbers")
for i in range(100):
    print("[",a + (b-a) * random(),"],[",c+ (d-c)* random(),"]")


