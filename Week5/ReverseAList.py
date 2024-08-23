n = int(input("Enter no.of elements : "))
li = []

for i in range(n) :
    li.append(int(input("Enter element : ")))
print("Before Reversing :", li)
print("After Reversing :",li[::-1])
