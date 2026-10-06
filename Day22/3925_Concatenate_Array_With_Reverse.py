def concatWithReverse(nums: list[int]) -> list[int]:
    rev = list(reversed(nums))

    return [*nums, *rev]

numbers = [1, 2, 3]
print(concatWithReverse(numbers))