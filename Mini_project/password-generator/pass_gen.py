import string
import random

def gen():
    s1= string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation

    pass_length=int(input("Enter Your password length: "))
   
    s= []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))

    random.shuffle(s)

    pasw = ("".join(s[0:pass_length]))

    print("Your password is : " , pasw)
    

gen()