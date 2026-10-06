n = int(input("Enter the size of the array: "))
candidates = [int(input("Enter the element: ")) for _ in range(n)]
target = int(input("Enter the target: "))
print(candidates)
print(target)

result = []

path = [(target, [], 0)]

while len(path) > 0:
    dummy, current_combo, start_idx = path.pop()

    for i in range(start_idx, len(candidates)):
        rem = dummy - candidates[i]

        if rem == 0:
            result.append(current_combo + [candidates[i]])

        elif rem > 0:
            path.append((rem, current_combo + [candidates[i]], i))

print(result)