n = int(input("Enter no.of elements : "))
li = []

for i in range(n) :
    li.append(int(input("Enter element : ")))
print("Position of Minimum Element :", li.index(min(li)))
print("Position of Maximum Element :", li.index(max(li)))

#output
Enter no.of elements : 5
Enter element : 8
Enter element : 1
Enter element : 4
Enter element : 3
Enter element : 6
Position of Minimum Element : 1
Position of Maximum Element : 0
