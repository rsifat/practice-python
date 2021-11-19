#with out using function

jemes_exp_list=[2,1,4,6,10]  #23
john_exp_list= [1,5,9,5,7]  #27

total1=0
total2=0


for item in jemes_exp_list:
    total1=total1+item
print("jemes exp list is ", total1)


for item in john_exp_list:
    total2=total2+item
print("john exp list is ", total2)


if total1>total2:
    print("jemes is rich")

elif total1 == total2:
    print("They are Equal")
else:
    print("john is rich")
