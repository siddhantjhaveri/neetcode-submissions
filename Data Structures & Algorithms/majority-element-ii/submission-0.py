class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count ={}
        res = []
        for i in nums:
            count[i]= count.get(i,0)+1
            if count[i] > len(nums)/3 and (i not in res):
                res.append(i)
        return res
        