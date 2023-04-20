'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
x=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y=[6.41, 9.27, 11.53, 14.56, 17.02, 20.45, 23.09, 25.12, 28.36, 30.80]
s=len(x)
s_x=sum(x)
s_y=sum(y)
xx=[]
yy=[]
xy=[]

for i in range(0, s):
    x_2=x[i]**2
    xx.append(x_2)
    y_2=y[i]**2
    yy.append(y_2)
    x_y=x[i]*y[i]
    xy.append(x_y)
    
s_xx=sum(xx)
s_yy=sum(yy)
s_xy=sum(xy)

delta=s*s_xx-s_x**2

alpha=(s*s_xy-s_x*s_y)/delta
beta=(s_xx*s_y-s_x*s_xy)/delta

print("Alpha = ", round(alpha, 3))
print("Beta = ", round(beta, 3))