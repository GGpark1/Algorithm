class Solution:
    def singleNumber(self, nums):
        num_dict = {}
        for i in nums:
            num_dict[i] = num_dict.get(i, 0) + 1

        for k, v in num_dict.items():
            if v == 1:
                return k