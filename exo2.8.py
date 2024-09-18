nums = [25,13,6,17,9]
n=nums[0]


for i in range(len(nums)):
    for y in range(len(nums)):
        if nums[i] < nums[y]:
            tempo = nums[i]
            nums[i] = nums[y]
            nums[y] = tempo
        
print(nums)
"""nums.sort()
print(nums)"