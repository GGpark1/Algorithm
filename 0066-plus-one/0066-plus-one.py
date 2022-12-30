class Solution:
    def plusOne(self, digits):

        total = ""

        for i in range(len(digits)):

            total += str(digits[i])

        total = str(int(total) + 1)

        res = []

        for j in total:
            res.append(int(j))

        return res
