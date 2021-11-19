# using_function

def calculate_total(exp):
    total = 0
    for item in exp:
        total = total + item
    return total


jemes_exp_list = [2, 1, 4, 6, 10]  # 23
john_exp_list = [1, 5, 9, 5, 7]  # 27

jemes_total = calculate_total(jemes_exp_list)
print("jemes exp is:", jemes_total)

john_total = calculate_total(john_exp_list)
print("john exp is:", john_total)

if jemes_total > john_total:
    print("jemes is rich")

elif jemes_total == john_total:
    print("They are Equal")
else:
    print("john is rich")
