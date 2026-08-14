class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        p = {')':'(','}':'{',']':'['}
        for i in s:
            if i in p:
                if stack and stack[-1] == p[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else False
        