class Solution:
    def digitSum(self, s: str, k: int) -> str:
        def sumDigits(x: int) -> int:
            res = 0
            while x:
                res += x % 10
                x //= 10

            return res

        while len(s) > k:
            splitting_string = [s[i : i + k] for i in range(0, len(s), k)]
            int_res = []
            for string in splitting_string:
                z = int(string)
                int_res.append(str(sumDigits(z)))
            s = "".join(int_res)

        return s