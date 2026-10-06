def findDegrees(matrix: list[list[int]]) -> list[int]:
    if not matrix:
        return []
    result = []

    for i in range(len(matrix)):
        result.append(matrix[i].count(1))

    return result

m = [[0]]

print(findDegrees(m))