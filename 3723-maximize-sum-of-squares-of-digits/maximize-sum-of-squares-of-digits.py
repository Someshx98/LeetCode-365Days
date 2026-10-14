class Solution:
    def maxSumOfSquares(self, num: int, sumN: int) -> str:
            if num * 9 < sumN:
                return ""

            nines = sumN // 9
            rem = sumN % 9

            result = "9" * nines

            if rem:
                result += str(rem)

            return result + "0" * (num - len(result))