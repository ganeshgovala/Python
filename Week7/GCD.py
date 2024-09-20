def gcd(num1, num2) : 
    if num1 % num2 == 0 :
        return num2
    else :
        return gcd(num2, num1 % num2)

num1 = int(input("Enter num1 : "))
num2 = int(input("Enter num2 : "))
print(gcd(num1, num2))

output : 
Enter num1 : 123
Enter num2 : 36
3
