n = int(input("Enter no.of elements : "))
li = []

for i in range(n) :
    li.append(int(input("Enter element : ")))
print("Before Swapping :", li)
temp = li[-1]
li[-1] = li[0]
li[0] = temp
print("After Swapping :", li)

#output
Enter no.of elements : 5
Enter element : 1
Enter element : 2
Enter element : 3
Enter element : 4
Enter element : 5
Before Swapping : [1, 2, 3, 4, 5]
After Swapping : [5, 2, 3, 4, 1]
