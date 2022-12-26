class Solution:
    def isValid(self, s):
        stack = []
        is_true = False

        for i in s:
            if i in ['(', '{','[']:
                stack.append(i)
            else:
                if not stack:
                    return is_true
                else:
                    if stack[-1] + i in ['()', '{}', '[]']:
                        stack.pop()
                    else:
                        return is_true

        if stack:
            return False
        else:
            is_true = True
            return is_true