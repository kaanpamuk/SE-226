def factorial(x):
    if x == 0 or x == 1:
        return 1
    else:
        return x * factorial(x - 1)
print(factorial(4))






def exp_x(x, n):
    step = lambda k: (x ** k) / factorial(k)
    sum = 0

    for k in range(n + 1):
        sum+= step(k)
    return sum
print(exp_x(1, 3))








a=0
def func(n):
    global a
    if n !=1 :
        a = (-1) ** (n+1) / n
        func(n - 1)
    a+=0.5
n =int(input("enter number"))
func(n)
print(a)



