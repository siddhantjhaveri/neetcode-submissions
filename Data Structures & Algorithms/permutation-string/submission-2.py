class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        r = len(s1)
        sub_s = s2[:r]
        l=0
        while r<=len(s2):
            if sorted(s1) == sorted(sub_s):
                return True
            else:
                l+=1
                r+=1
                sub_s = s2[l:r]
        return False
        