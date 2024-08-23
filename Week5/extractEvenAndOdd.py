n = int(input("Enter no.of elements : "))
li = []

for i in range(n) :
    li.append(int(input("Enter element : ")))
even = []
odd = []
for i in li :
    if i%2 == 0 :
        even.append(i)
    else :
        odd.append(i)
print("Even :", even)
print("Odd :", odd)

#output
Enter no.of elements : 5
Enter element : 4
Enter element : 2
Enter element : 6
Enter element : 1
Enter element : 3
Even : [4, 2, 6]
Odd : [1, 3]
