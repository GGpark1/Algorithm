class Solution:
    def majorityElement(self, nums):

        count = 0
        major = None
        for num in nums:
            if count == 0:
                major = num
            count += 1 if major == num else -1
        return major
