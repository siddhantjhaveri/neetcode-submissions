class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minsub = float('inf')
        l=0
        r=0
        sum_ = 0
        while r<len(nums):
            sum_ += nums[r]
            while sum_ >= target: 
                sum_ = sum_ - nums[l]
                minsub = min(r-l+1, minsub)
                l=l+1
            r+=1
        return 0 if minsub == float('inf') else minsub


        