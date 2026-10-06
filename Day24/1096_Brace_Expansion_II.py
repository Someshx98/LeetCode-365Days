class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        self.s = expression
        self.n = len(expression)
        self.idx = 0

        st = self.performUnion()
        return sorted(st)

    def getUnit(self):
        result = set()

        if self.s[self.idx] == '{':
            self.idx += 1
            result = self.performUnion()
        else:
            result = {self.s[self.idx]}

        self.idx += 1
        return result

    def performConcat(self):
        result = {""}

        # Note: in Python we must guard idx < n before indexing s[idx],
        # since Python strings don't allow the "one past the end" access
        # that C++'s std::string::operator[] permits.
        while self.idx < self.n and (self.s[self.idx] == '{' or self.s[self.idx].isalpha()):
            temp = self.getUnit()

            concatResult = set()
            for left in result:
                for right in temp:
                    concatResult.add(left + right)
            result = concatResult

        return result

    def performUnion(self):
        result = set()

        while True:
            temp = self.performConcat()
            result |= temp

            if self.idx < self.n and self.s[self.idx] == ',':
                self.idx += 1
            else:
                break

        return result