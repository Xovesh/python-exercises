def isPalindrome(s):
    if len(s) == 0:
        return True
    elif s[0] != s[-1]:
        return False
    else:
        return isPalindrome(s[1:-1])


s = "kinikinik"
print(s, isPalindrome(s))
s = "asantaatnasa"
print(s, isPalindrome(s))
s = "aba"
print(s, isPalindrome(s))
s = ""
print(s, isPalindrome(s))
s = "aa"
print(s, isPalindrome(s))
s = "abc"
print(s, isPalindrome(s))
s = "ac"
print(s, isPalindrome(s))