def issubstring(word, sub):
    if word == "":
        return True

    elif word != "" and sub == "":
        return False

    else:
        return (word[-1] == sub[-1] and word[:-1] == sub[-(len(word[:-1])+1):-1]) or issubstring(word, sub[:-1])


a = "abba"
b = "abbbaabba"
print(issubstring(a, b))
print(a in b)
