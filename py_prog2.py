def addstring(word1 , word2):
    newString = ""
    length = len(word1)
    for i in range(length + 1):
        if i < length // 2 :
            newString += word1[i]
        elif i == length //2 :
            newString += word2
        else :
            newString += word1[i - 1]
    return newString
string1 = str(input("Write the first word: "))
string2 = str(input("Write the second word: "))
print(addstring(string1, string2))