n = int(input("Enter no.of elements : "))
li = []

for i in range(n) :
    li.append(int(input("Enter element : ")))
print("Before Reversing :", li)
print("After Reversing :",li[::-1])

#output
Enter no.of elements : 5
Enter element : 1
Enter element : 2
Enter element : 3
Enter element : 4
Enter element : 5
Before Reversing : [1, 2, 3, 4, 5]
After Reversing : [5, 4, 3, 2, 1]
