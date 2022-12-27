class Solution:
    def removeDuplicates(self, nums):
        start = 0
        end = 0
        k = 1
        for i in range(1, len(nums)):
            end += 1
            if nums[start] == nums[end]:
                nums[end] = 101
            else:
                start = end
                k += 1

        nums.sort()

        return k
