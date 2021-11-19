import math

b=int(input("Enter The value of b :"))
a=int(input("Enter The value of a :"))
c=int(input("Enter The value of c :"))


def quad ():
    x1= (-b+ math.sqrt(b**b-4*a*c))/(2*a)
    x2= (-b- math.sqrt(b**b-4*a*c))/(2*a)

    z1='{0:.3f}'.format(x1)
    z2='{0:.3f}'.format(x2)
 
    return z1 , z2
    

k=quad()

print("The output value is :",k)

#why Why.....




