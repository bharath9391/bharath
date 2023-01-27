"""def cube(x):
    y=x**3
    return y
x=8
y=4
z=cube(x)-cube(y)
print(z)"""

"""def smallest(a,b,c):
    if a<=b:
        if a<=c:
            smallest=a
        else:
            smallest=c
    else:
        if b<=c:
            smallest=b
        else:
            smallest=c

    return smallest
a=int(input("enter the number"))
b=int(input("enter the number"))
c=int(input("enter the number"))
m=smallest(a,b,c)
print(m)"""


def largest(a,b,c):
    if a>=b:
        if a>=c:
            largest=a
        else:
            largest=c
    else:
        if b>=c:
            largest=b
        else:
            largest=c

    return largest
a=int(input("enter the number"))
b=int(input("enter the number"))
c=int(input("enter the number"))
m=largest(a,b,c)
print(m)




        
        
      



        
        
      
