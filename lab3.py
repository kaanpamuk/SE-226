x = int(input("Enter a number greater than 1"))
step=0
while x!=1:
    if x % 2 == 0:
        x= x//2
    else:
        x=x*3+1

    print("-->",x,end=" ")
    step=step+1
print("total step is :", step)

