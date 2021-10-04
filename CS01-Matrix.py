import numpy as np
arry=[]
array=[]
m=int (input(" ป้อนข้อมูล(height) "))
n=int (input(" ป้อนข้อมูล(width) "))
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