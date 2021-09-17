import numpy as np
arry=[]
array=[]
m=int (input("enter the height you want for ur matrix to be "))
n=int (input("enter the width you want for ur matrix to be "))
x=m*n
print ("enter number for your first array")
for i in range(x):
    arry+=[int(input(""))]
NewAray = np.asarray(arry)
print ("enter number for your second array")
for j in range(x):
    array+=[int(input(""))]
NewAray = np.asarray(array)
NewArray = np.asarray(arry)
NewArrayNumpy = NewArray.reshape(int(m),n)
print(NewArrayNumpy)
NewArryNumpy = NewAray.reshape(int(n),m)
print(NewArryNumpy)
y=np.add(NewArrayNumpy,NewArryNumpy)
print(y)
