def calc(num1, num2, op) :
    return eval(f'{num1} {op} {num2}')
num1 = int(input("Enter num1 : "))
num2 = int(input("Enter num2 : "))
op = input("Enter operation : ")
print(calc(num1, num2, op))

output : 
Enter num1 : 3
Enter num2 : 6
Enter operation : +
9
