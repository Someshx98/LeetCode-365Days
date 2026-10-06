numbers = "23456789"

res = []

digits = input("Enter a number: ")

phone_map = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz"
}

def answer(index, current_str):
    if len(current_str) == len(digits):
        res.append(current_str)
        return

    possible_letter = phone_map[digits[index]]

    for letter in possible_letter:
        answer(index + 1, current_str + letter)

    return res


if not digits:
    res = []
else:
    answer(0, "")

print(res)