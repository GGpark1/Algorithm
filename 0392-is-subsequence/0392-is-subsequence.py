class Solution:
    def isSubsequence(self, s: str, t: str):
        subsequence = 0
        for i in range(0, len(t)):
            if subsequence <= len(s) - 1:
                if s[subsequence] == t[i]:

                    subsequence += 1
        return subsequence == len(s)