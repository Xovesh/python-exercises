
# recursive version 85% acceptance
def isNumber(s):
    valideverywhere = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", " "]
    valid = ["e", "+", "-", "."]
    if s == "":
        return True
    else:
        if len(s) >= 3:
            last = s[len(s) - 1]
            anteccesor = s[len(s) - 2]
            rest = s[0:-2]
        elif len(s) == 2:
            last = s[len(s) - 1]
            anteccesor = s[len(s) - 2]
            rest = ""
        else:
            last = s
            anteccesor = ""
            rest = ""
        if last in valideverywhere:
            if anteccesor in valid:
                result = isNumber(rest)
            else:
                result = isNumber(rest + anteccesor)
        else:
            return False
    return result

# Deterministic finite automata 100% acceptance
def isNumber2(s):
    DFA = [{"blank": 0, "sign": 2, "dot": 3, "number": 1},
           {"number": 1, "dot": 4, "e": 5, "blank": 7},
           {"number": 1, "dot": 3},
           {"number": 4},
           {"number": 4, "e": 5, "blank": 7},
           {"sign": 6, "number": 8},
           {"number": 8},
           {"blank": 7},
           {"number": 8, "blank": 7}
           ]

    currentstate = 0
    state = ""
    for i in s:
        if i in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            state = "number"
        elif i == " ":
            state = "blank"
        elif i == "+" or i == "-":
            state = "sign"
        elif i == "e":
            state = "e"
        elif i == ".":
            state = "dot"
        if state not in DFA[currentstate].keys():
            return False
        currentstate = DFA[currentstate][state]
        state = ""

    if currentstate in [1, 7, 4, 8]:
        return True
    else:
        return False
