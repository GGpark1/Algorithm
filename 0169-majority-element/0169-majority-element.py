class Solution:
    def majorityElement(self, nums):
        dic = {}
        for i in nums:
            dic[i] = dic.get(i, 0) + 1

        max = 0
        for k, v in dic.items():
            if v > max:
                max = v
                major = k

        return major
        