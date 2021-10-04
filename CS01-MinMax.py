Num = int(input('Enter your loops:'))
Numtotal = []
for i in range(Num) :
    data = int(input('Enter your Data:'))
    Numtotal += [data]
Numtotal.sort()
min= Numtotal[0]
print('Minimum Number is:',min)
max = Numtotal[Num-1]
print('Maximum Number is', max)