def groupAnagrams(arr):
    dict={}
    result=[]
    for word in arr:
        sortedword ="".join(sorted(word))
        dict.setdefault(sortedword,[])
        if sortedword not in dict:
            dict["sortedword"] = word
        else:
            dict[sortedword].append(word)
    for item in dict.values():
        result.append(item)
    return result
    


arr= ["eat", "tea", "tan", "ate", "nat", "bat"]
print groupAnagrams(arr)
