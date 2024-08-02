a = int(input("Enter number : "))
original = a
temp = 0

while(a > 0) :
    temp = temp * 10 + (a % 10)
    a = a // 10
if original == temp :
    print("Palindrome")
else :
    print("Not a palindrome")

#output
Enter number : 12321
Palindrome
