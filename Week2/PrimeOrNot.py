n = int(input("Enter number : "))
count = 0
for i in range(1, n+1) :
    if(n % i == 0) :
        count += 1
if(count == 2) :
    print("Prime Number")
else :
    print("Not a Prime Number")

#output
Enter number : 5
Prime Number
