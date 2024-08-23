n = int(input("Enter no.of elements : "))
li = []

for i in range(n) :
    li.append(int(input("Enter element : ")))
print("Sum of given Elements is :", sum(li))
print("Average of given Elements is :", sum(li) / len(li))

#ouput
Enter no.of elements : 5
Enter element : 1
Enter element : 2
Enter element : 3
Enter element : 4
Enter element : 5
Sum of given Elements is :  15
Average of given Elements is :  3.0
