def reverseList(li) :
    start = 0
    end = len(li) - 1
    while(start < end) :
        temp = li[start]
        li[start] = li[end]
        li[end] = temp
        start += 1
        end -= 1
    return li
print(reverseList([1,2,3,4,5,6,7,8]))
