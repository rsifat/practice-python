s = input("Enter your string:") # s is a string , we check string = string , not int

reverse = s[::-1] # its called slice , 3rd bracket 

if reverse == s:
    print ("It is a Palindrome")

else :
    print("It is not a Palindrome")
