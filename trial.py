
def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    i = 0
    j = len(nums)-1
    dict = {}
    for i in range(j+1):
        dict.update({nums[i]:i})
    nums.sort()
    while nums[i]+nums[j] != target:
        if nums[i] + nums[j] < target:
            i += 1
        else:
            j -= 1
    return [dict[nums[i]], dict[nums[j]]]

nums = [2,5,5,11]
target = 10
twoSum(nums,target)