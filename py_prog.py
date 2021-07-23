"""
Function gets string parametrs and returnes a new streang made of middle three characters.
Parametrs
---------
word -> str and odd

Return
--------
newWord -> str
"""
def strconvert(word):
    if (len(word) % 2 == 1):
        newWord = " "
        for i in range( ( (len(word) // 2 ) -1 ) , ( (len(word) // 2 ) + 2 )):
            newWord += word[i]
        return newWord
    else :
        return "type in incorect,you wrote even, please write odd"
word1 = str(input("Write the word: "))
print(strconvert(word1))