def fact(n) : 
    if n == 1 :
        return 1
    else :
        return n * fact(n - 1)
num = int(input("Enter number : "))
if num < 1 : 
    print("Factorial is not possible for less than 1")
else :
    print("Factorial is :",fact(num))

ouput : 
Enter number : 5
Factorial is : 120
