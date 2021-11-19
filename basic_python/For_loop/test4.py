#useing break statement

key_location="garage"
location= ["chair", "Table", "garage","book self"]

for i in location:
    if i==key_location:
        print("Key is found the ",i )
        break
    else:
        print("key is not found", i)