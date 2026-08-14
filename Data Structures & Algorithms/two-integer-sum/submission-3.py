class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_ = defaultdict(int)
        for i in range(len(nums)):
            j = target - nums[i]
            if j in dict_:
                return [dict_[j],i]
            else:
                dict_[nums[i]] = dict_.get(nums[i],0) + i     