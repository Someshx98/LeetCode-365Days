m = int(input("Enter the number of rows: "))
n = int(input("Enter the number of columns: "))

box = []

for row in range(m):
    mid_box = []
    for col in range(n):
        x = int(input("Enter the element: "))
        mid_box.append(x)
    box.append(mid_box)

# for row in range(m):
#     print(box[row])

search = int(input("Enter the target: "))

# def search_matrix(matrix: list[list[int]], target: int) -> bool:
#     row, col = len(matrix), len(matrix[0])
#     for r in range(row):
#         if target in matrix[r]:
#             return True
#         else:
#             continue
#
#     return False

def search_matrix(matrix: list[list[int]], target: int) -> bool:
    if not matrix or not matrix[0]:
        return False

    m, n = len(matrix), len(matrix[0])
    left, right = 0, (m * n) - 1

    while left <= right:
        mid = (left + right) // 2
        mid_val = matrix[mid // n][mid % n]

        if mid_val == target:
            return True
        elif mid_val < target:
            left = mid + 1
        else:
            right = mid - 1

    return False

print(search_matrix(box, search))