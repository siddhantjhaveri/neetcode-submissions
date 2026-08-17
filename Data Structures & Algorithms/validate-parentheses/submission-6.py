class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        a = {'}':'{',')':'(',']':'['}
        for i in s:
            if i in a:
                if not stack or stack.pop() != a[i]:
                    return False
                else:
                    continue
            else:
                stack.append(i)
            print(stack)
        if len(stack)==0:
            return True
        else:
            return False
        