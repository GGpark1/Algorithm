
class Solution:
    def twoSum(self, nums, target):
        dict = {}
        for i in range(len(nums)):
            comple_num = target - nums[i]
            if comple_num in dict:
                       return [dict[comple_num], i]
            else:
                dict[nums[i]] = i

        