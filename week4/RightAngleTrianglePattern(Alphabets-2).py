n=int(input("enter no of rows:"))
m = 65
for i in range(1,n+1) :
    for j in range(i) :
        print(chr(m),end=' ')
        m+=1
    print('')
