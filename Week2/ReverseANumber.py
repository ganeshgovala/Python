a = int(input("Enter number : "))
temp = 0

while(a > 0) :
    temp = temp * 10 + (a % 10)
    a = a // 10
print("After Reversing : ", temp)

#output
Enter number : 12345
After Reversing : 54321
