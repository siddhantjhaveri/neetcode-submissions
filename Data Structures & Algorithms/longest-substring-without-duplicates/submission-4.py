class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxs = 0
        l=0
        r=0
        ind = {}
        while r<len(s):
            if s[r] in ind and ind[s[r]] >= l:
                l = ind[s[r]]+1
                ind[s[r]] = r
            else:
                ind[s[r]] = r
            maxs = max(r-l+1,maxs)
            r+=1
        return maxs
        