from ast import Break


x=int(input("Enter year:"))

if x%4==0:
    print(x," is leap year ")

    

      
elif x%100==0:
    print(x," is leap year ")

    

elif x%400==0:
    print(x," is leap year ")

   

else:
    print(x," is not a leap year")