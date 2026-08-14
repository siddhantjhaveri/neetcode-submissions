class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        for j in range(len(nums)-3):
            if j>0 and nums[j-1]==nums[j]:
                continue
            for i in range(j+1,len(nums)-2):
                if i>j+1 and nums[i-1]==nums[i]:
                    continue
                l = i+1
                r = len(nums)-1
                k = nums[j]+nums[i]
                while l<r:
                    n = nums[l]+nums[r]
                    t = target-k
                    if n>t:
                        r-=1
                    elif n<t:
                        l+=1
                    else:
                        res.append([nums[j],nums[i],nums[l],nums[r]])
                        while l<r and nums[l]==nums[l+1]:
                            l+=1
                        while l<r and nums[r]==nums[r-1]:
                            r-=1
                        l+=1
                        r-=1
        return res
        