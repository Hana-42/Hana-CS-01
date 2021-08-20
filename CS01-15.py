def my_list(lis):
    i = 0
    for i in range (len(lis)):
        if lis[i]==20:
            lis[i]=200
    print(lis)
lis=[5,10,15,20,25,50,20]
my_list(lis)