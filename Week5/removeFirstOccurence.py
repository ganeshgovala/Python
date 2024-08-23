n = int(input("Enter no.of elements : "))
li = []

for i in range(n) :
    li.append(int(input("Enter element : ")))
target = int(input("Enter number to delete : "))
if target in li :
    print("Before Removing :", li)
    li.remove(target)
    print("After Removing :",li)
else :
    print("There is no",target,"in the given Elements")

#output1
Enter no.of elements : 5
Enter element : 1
Enter element : 1
Enter element : 2
Enter element : 2
Enter element : 4
Enter number to delete : 1
Before Removing : [1, 1, 2, 2, 4]
After Removing : [1, 2, 2, 4]

#output 2
Enter no.of elements : 5
Enter element : 1
Enter element : 2
Enter element : 3
Enter element : 4
Enter element : 5
Enter number to delete : 6
There is no 6 in the given Elements
