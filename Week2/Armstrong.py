n = int(input("Enter the number : "))
original = n
sum = 0
while n > 0 :
    rem = n % 10
    sum += rem ** 3
    n = n // 10
if sum == original :
    print("Armstrong number")
else :
    print("Not an Armstrong Number")

#output
Enter the number : 153
Armstrong number
