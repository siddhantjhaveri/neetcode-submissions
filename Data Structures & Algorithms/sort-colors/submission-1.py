class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # for i in range(len(nums)-1):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]>nums[j]:
        #             nums[i],nums[j] = nums[j],nums[i]
        count = [0]*3
        for i in nums:
            count[i] +=1
        id = 0
        for j in range(3):
            while count[j]>0:
                nums[id] = j
                id+=1
                count[j]-=1

        