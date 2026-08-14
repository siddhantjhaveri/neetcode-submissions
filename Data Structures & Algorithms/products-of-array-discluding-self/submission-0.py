class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr = []
        l,r = 1,1
        arr = []
        for i in range(len(nums)):
            lp , rp = i,i
            while lp > 0:
                lp = lp-1
                l = l * nums[lp]
            while rp < (len(nums)-1):
                rp = rp+1
                r = r * nums[rp]
            arr.append(l*r)
            l,r = 1,1
        return arr


        