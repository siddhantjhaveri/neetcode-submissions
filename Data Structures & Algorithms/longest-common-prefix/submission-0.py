class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        a = strs[0]
        c = 0
        while c<len(min(strs)):
            for i in strs[1:]:
                if i[c]==a[c]:
                    continue
                else:
                    return a[0:c]
            c+=1
        return a[0:c]