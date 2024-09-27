def fibonacci(n) :
    if n <= 1 :
        return n
    else :
        return fibonacci(n - 1) + fibonacci(n - 2)
num = int(input("Enter No.of digits you require : "))
for i in range(num) :
    print(fibonacci(i), end = " ")

output : 
Enter No.of digits you require : 5
0 1 1 2 3
