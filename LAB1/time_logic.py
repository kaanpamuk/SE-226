x =int(input('Enter a number: '))
hour=x // 3600
temp=x % 3600
minute=temp // 60
second=temp % 60
print(x ,'second is', hour ,'hour', minute ,'minute', second ,'second')