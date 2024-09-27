thisDict = {
    "name" : "Ganesh",
    "age" : 18
}

def findTheKey(target) :
    for key in thisDict.keys() :
        if(key == target) :
            return 'Found'
    return "Not Found"
    
print(findTheKey("name"))

output : 
Found
