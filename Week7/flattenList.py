def flattenList(li, res) :
    for i in li :
        if(type(i) == list) :
            flattenList(i, res)
        else :
            res.append(i)
    return res
print(flattenList([2,[1,[5,6]], [3,[4,[5]]]], []))

output : 
[2, 1, 5, 6, 3, 4, 5]
