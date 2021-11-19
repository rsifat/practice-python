indian=["rice", "dal", "patato"]
bangla=["egg", "fish","pitha"]
chinise=["fried rice" , "milk bread", "egg role"]

dish = input("Enter dish name: ")

if dish in bangla:
    print("This dish is bangladeshi")
elif dish in indian:
    print("This dish is indian ")
elif dish in chinise:
    print("This dish is chinise")
else:
    print("Write The currect dish name")