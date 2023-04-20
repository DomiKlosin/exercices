import random
import math

n=int(input("Enter the number of iteration to calculate the value of pi: "))

po=0
p=0
for i in range(0, n):
    x=random.uniform(0, 1)
    y=random.uniform(0, 1)
    d=x**2+y**2
    if d<1:
        po=po+1
        p=p+1
    else:
        p=p+1
    pi=math.pi
    value_pi=4*(po/p)
    diff=abs((pi-value_pi)/pi)

print("Calculated value of pi: ", value_pi)
print("Diff value: ", diff)
