number = int(input("Enter The Number :"))

if number < 1:
    print("Number needs to be greater than 1")

elif number == 1:
    print(number," is neither a prime or composit number")

else:
    for devisor in range (2,int(number/2)+1):
        if (number%devisor)==0:
            print(devisor) # why we use break?
            print(number,"is a composit number")
            break  # Ans: when get first devisor , then it will never check 
    
        else:
            print(number,"is a prime number")

