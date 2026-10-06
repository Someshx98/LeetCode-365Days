def moveZeros(nums: list[int]) -> None:
    # i, j = 0, len(nums) - 1
    #
    # while i < j:
    #     if nums[i] == 0:
    #         nums[i], nums[j] = nums[j], nums[i]
    #         i += 1
    #         j -= 1
    #
    #     else:
    #         i += 1

    k = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[k], nums[i] = nums[i], nums[k]
            k += 1

x = [0,1,0,3,12]
moveZeros(x)
print(x)