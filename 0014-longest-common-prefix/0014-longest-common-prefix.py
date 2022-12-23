class Solution:
    def longestCommonPrefix(self, strs):

        short = min(strs, key=len)

        for str in strs:
            while len(short) > 0:
                if str.startswith(short):
                    break
                else:
                    short = short[:-1]

        return short
