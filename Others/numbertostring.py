def numbertostring(number, method):
    numbercount = 0
    stringnumber = ""
    while number > 0:
        if numbercount in method:
            stringnumber += ","
        stringnumber += str(number % 10)
        number = number // 10
        numbercount += 1
    return stringnumber[::-1]


us = set()
us.add(3)
us.add(6)
us.add(9)
us.add(15)
id = set()
id.add(3)
id.add(5)
id.add(7)
id.add(9)
id.add(11)
id.add(13)

print(numbertostring(1000, id))

