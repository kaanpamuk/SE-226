n = int(input("enter  number between 3 and 9: "))

while n < 3 or n > 9:
    n = int(input("please enter a number between 3 and 9: "))

for i in range(1, n+1):
    for j in range(i):
        print("*", end="")
    print()

for i in range(n-1, 0, -1):
    for j in range(i):
        print("*", end="")
    print()