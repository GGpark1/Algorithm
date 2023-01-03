class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2

        li = [0] * (n+1)
        li[1] = 1
        li[2] = 2
        for i in range(3, n+1):
            li[i] = li[i-1] + li[i-2]

        return li[n]
