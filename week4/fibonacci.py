n = int(input())
one = 0
two = 1
if n == 0 or n == 1 :
    print(0)
else :
    print(one, end=" ")
    print(two, end=" ")
    for i in range(n - 2) :
        x = one + two
        print(x, end=" ")
        one = two
        two = x
