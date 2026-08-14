class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n = len(nums)
        # Phase 1: Place every number in its "home" position using swaps
        for i in range(n):
            # While this number is a valid locker number (1 to n)
            # AND the locker it belongs to doesn't already have this number
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                # Calculate the index where this number *should* live
                correct_index = nums[i] - 1
                # Swap it to its home
                nums[i], nums[correct_index] = nums[correct_index], nums[i]
                # The 'while' loop continues to check the new number we brought back
                
        # Phase 2: Find the first locker that is empty/wrong
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1  # Locker number is missing
                
        # Phase 3: All lockers 1 to n are filled perfectly
        return n + 1