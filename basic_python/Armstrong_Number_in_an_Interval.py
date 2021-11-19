n1=int(input("Enter The lower Number:"))
n2=int(input("Enter The Upper Number:"))

for num in range(n1, n2 + 1):

   # order of number
   order = len(str(num))
    
   # initialize sum
   sum = 0

   temp = num
   while temp > 0:
       digit = temp % 10
       sum += digit ** order
       temp //= 10

   if num == sum:
       print(num)


