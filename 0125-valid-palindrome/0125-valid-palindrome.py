import re

class Solution:
    def isPalindrome(self, s):

        li = re.findall('[a-zA-Z0-9]', s)
        li = list(map(lambda x: x.lower(), li))

        total = len(li)
        div_ind = total//2

        if total % 2 == 0:
            left = li[:div_ind]
            right = li[div_ind:]
        else:
            left = li[:div_ind]
            right = li[div_ind+1:]

        right = right[::-1]

        if left == right:
            return True
        else:
            return False
