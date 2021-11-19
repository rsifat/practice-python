# sum of two numbers using function

def sum(b, a):
    print("a is :", a)
    print("b is :", b)
    total = a + b
    print("total inside function:", total)
    return total

n1 = sum(1, 6)
print("total- outside", n1)


n2=sum(100,12)
print("total", n2)


if n2>n1:
    print("n2 is high")
