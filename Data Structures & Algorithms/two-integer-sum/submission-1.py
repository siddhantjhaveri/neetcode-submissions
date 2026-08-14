class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # # 2 for loops over array
        # for i in range(len(nums)-1):
        #     for j in range(i,len(nums)):
        #         if nums[i]+nums[j]==target:
        #             return [i,j]
        a = {}
        for i in range(len(nums)):
            b = target-nums[i]
            print(f"b = {b}")
            if b in a:
                return [a[b],i]
            else:
                a[nums[i]] = i
            print(f"a = {a}")
        