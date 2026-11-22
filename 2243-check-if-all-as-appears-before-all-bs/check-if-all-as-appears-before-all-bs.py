class Solution:
    def checkString(self, s: str) -> bool:
        b_1st = len(s)
        for i in range(len(s)):
            if s[i] == "b":
                b_1st = i
                break

        for i in range(b_1st, len(s)):
            if s[i] == "a":
                return False

        return True