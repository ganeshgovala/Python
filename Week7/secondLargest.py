def secondLargest(li) :
    li.sort()
    se = set(li)
    li = list(se)
    return li[-2]
print(secondLargest([1,2,3,4,5,6,6,7,7,7,8,8,9,9,9]))

output : 
8
