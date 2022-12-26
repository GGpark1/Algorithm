class Solution:
    def isValid(self, s):
        stack = []
        bracket_dic = dict(('()', '{}', '[]'))

        for i in s:
            if i in ['(', '{','[']:
                stack.append(i)
            else:
                if not stack or i != bracket_dic[stack[-1]]:
                    return False
                else:
                    stack.pop()
        
        return len(stack) == 0
                
        