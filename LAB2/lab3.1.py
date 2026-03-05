x= int(input("enter the number between 10 and 100"))
while x < 10 or x > 100:
    x = int(input("enter the number between 10 and 100"))

fizz=0
buzz=0
fizzbuzz=0
for i in range(1,x+1):
    if i % 7 == 0:
        continue
    if i%3==0 and i%5==0:
        print("fizzbuzz")
        fizzbuzz=fizzbuzz+1
    elif i%3==0:
            print("fizz")
            fizz=fizz+1
    elif i%5==0:
            print("buzz")
            buzz=buzz+1
    else:
            print(i)
print("Finally\n")
print("Fizz count ",fizz )
print("Buzz count ",buzz)
print("Fizzbuzz count ",fizzbuzz)




