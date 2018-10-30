a,b = 0,1
while a < 10:
    print(a)
    a,b = b, a+b
print('-------------------------------------------------')
i = 256*256
print('the value of i is ', i)

print('-------------------------------------------------')
a,b = 0,1
while a < 1000:
    print(a, end='# ')
    a,b = b, a+b

print('-------------------------------------------------')
x = int(input("please enter an integer: "))
if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x ==1:
    print('Single')
else:
    print('More..!!')

