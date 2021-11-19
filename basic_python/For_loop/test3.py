exp= [1254,1454,225, 2231,4521,4568,2214,1235]
total= 0
for i in range(len(exp)):
    print('Month:',(i+1), 'Expense:', exp[i])
    total = total + exp[i]
print("My Total Expenses : ", total)