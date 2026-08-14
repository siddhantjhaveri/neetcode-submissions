class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = {}
        for i in nums:
            c[i] = c.get(i,0)+1
        for i,j in c.items():
            if j > len(nums)/2:
                return i

        