class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        setn = set()
        for num in nums:
            if num in setn:
                return True
            setn.add(num)
        return False
        