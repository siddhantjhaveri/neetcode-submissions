class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        # i=0
        # tp = 1
        # while i<len(nums):
        #     for v in range(len(nums)):
        #         if i == v:
        #             continue
        #         else:
        #             tp = tp*nums[v]
        #     i+=1
        #     res.append(tp)
        #     tp=1
        # return res
        lt = [1]*len(nums)
        for i in range(1,len(nums)):
            lt[i] = nums[i-1]*lt[i-1]
        print(lt)
        rt = [1]*len(nums)
        for j in range(len(nums)-2,-1,-1):
            rt[j] = nums[j+1]*rt[j+1]
        print(rt)
        for k in range(len(nums)):
            res.append(lt[k]*rt[k])
        return res