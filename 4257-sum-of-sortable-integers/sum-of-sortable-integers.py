class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        size = len(nums)
        if size == 0:
            return 0

        divisors = [i for i in range(1, size + 1) if size % i == 0]
        result = 0

        for divisor in divisors:
            possible = True
            prev_max = -float("inf")

            for start in range(0, size, divisor):
                end = start + divisor
                drops = 0
                drop_index = -1

                for i in range(start, end - 1):
                    if nums[i] > nums[i + 1]:
                        drops += 1
                        drop_index = i
                        if drops > 1:
                            break

                if drops > 1:
                    possible = False
                    break

                if drops == 0:
                    current_min, current_max = nums[start], nums[end - 1]

                else:
                    if nums[end - 1] > nums[start]:
                        possible = False
                        break
                    current_min, current_max = nums[drop_index + 1], nums[drop_index]

                if current_min < prev_max:
                    possible = False
                    break

                prev_max = current_max

            if possible:
                result += divisor

        return result