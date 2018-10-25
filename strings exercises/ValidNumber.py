class Solution:
    def isNumber(self, s):
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
                    result = self.isNumber(rest)
                else:
                    result = self.isNumber(rest + anteccesor)
            else:
                return False
        return result
