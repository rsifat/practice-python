

x=int(input("Enter your Number :"))



def fact():
    f=1
    for i in range (1,x+1):
        f=f*i
    return f


result=fact()

print("The factorial Number IS :",result)


