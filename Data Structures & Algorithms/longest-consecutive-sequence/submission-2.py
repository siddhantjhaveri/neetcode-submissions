class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        store = set(nums)
        for num in nums:
            streak, curr = 0, num
            print(f"streak - {streak} curr - {curr}")
            while curr in store:
                streak += 1
                curr += 1
                print(f"if in store the streak - {streak} curr - {curr}")
            print(f"res - {res}, streak - {streak}")
            res = max(res, streak)
        return res