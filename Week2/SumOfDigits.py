n = int(input("Enter number : "))
sum = 0
while n > 0 :
    sum += n % 10
    n = n // 10
print("Sum of Digits : ",sum)

#output
Enter number : 12554
Sum of Digits : 17
