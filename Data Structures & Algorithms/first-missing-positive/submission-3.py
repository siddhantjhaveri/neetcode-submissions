class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        missing = 1
        seen = [0]*(len(nums)+1)
        print(seen)
        for i in nums:
            if i>0 and i<len(nums)+1:
                seen[i-1] = 1
        print(seen)
        for i in range(len(seen)):    
            if not seen[i]:
                return i+1    