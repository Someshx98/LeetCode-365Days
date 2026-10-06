x = input("Enter the string: ")

# def partition(s: str) -> list[list[str]]:
#     res = []
#
#     splits = {
#         n : [s[i : i + n]for i in range(0, len(s), n)]
#         for n in range(1, len(s) + 1)
#     }
#
#     for k, v in splits.items():
#         p = []
#         for hot in v:
#             if hot == hot[::-1]:
#                 p.append(hot)
#
#         if len(p) == len(v):
#             res.append(p)
#
#     return res

def partition(s: str) -> list[list[str]]:
    res = []

    def backtrack(start: int, current_partition: list[str]):
        # Base case: reached the end of the string
        if start == len(s):
            res.append(current_partition.copy())
            return

        # Explore all possible substrings starting from 'start'
        for end in range(start + 1, len(s) + 1):
            substring = s[start:end]

            # Check if current substring is a palindrome
            if substring == substring[::-1]:
                # Choose: Add substring to path
                current_partition.append(substring)

                # Explore: Recurse for the remaining substring
                backtrack(end, current_partition)

                # Backtrack: Remove substring to try other partitions
                current_partition.pop()

    backtrack(0, [])
    return res

print(partition(x))