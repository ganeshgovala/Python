def reverseList(li) :
    res = []
    for i in li :
        res.insert(0, i)
    return res
print(reverseList([1,2,3,4,5,6,7,8]))
