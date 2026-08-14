class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s0 = strs[0]
        c = 0
        while c<len(s0):
            for s in strs[1:]:
                if c < len(s) and s0[c]==s[c]:
                    continue
                else:
                    return s0[:c]
            c+=1
        return s0
            
        