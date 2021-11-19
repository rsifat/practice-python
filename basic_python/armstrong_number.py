n=int(input("Enter A Number: "))

sum = 0

order = len(str(n))

copy_n = n

while (n>0):
    digit = n%10
    sum += digit ** order
    n= n//10

if (sum == copy_n):
    print("This is a armstrong number")

else :
    print("This is not a ar armstrong Number")