def mapWordWeights(words : list[str], weights: list[int]) -> str:
    given = "".join(words)

    original_map = {chr(i): 122 - i for i in range(97, 123)}
    given_map = {chr(97 + i): weights[i] for i in range(26)}

    # print(given_map)
    # print(original_map)

    mid_string = []

    for word in words:
        count = 0
        for ch in word:
            count += given_map[ch]
        mid_res = count % 26
        print(mid_res)

        key = next((k for k, v in original_map.items() if v == mid_res))
        print(key)
        mid_string.append(key)


    return "".join(mid_string)


given_string = ["abcd"]
given_weights = [7,5,3,4,3,5,4,9,4,2,2,7,10,2,5,10,6,1,2,2,4,1,3,4,4,5]
print(mapWordWeights(given_string,given_weights))