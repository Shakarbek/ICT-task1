def reverseLookup(dictionary, value):
    keys1=[]
    for k in dictionary.keys():
        if dictionary[k]==value:
            keys1.append(k)
    return keys1

dict={
    "a": "A",
    "b": "B",
    "c": "C",
    "b1": "B"
}
print(reverseLookup(dict, 'B'))