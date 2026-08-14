class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n  # Handle massive k
        
        # Helper function to reverse a portion of the array in-place
        def reverse(start: int, end: int) -> None:
            while start < end:
                # Swap the two ends
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        
        # The 3-step magic
        reverse(0, n - 1)      # Reverse whole array
        reverse(0, k - 1)      # Reverse first k
        reverse(k, n - 1)      # Reverse the rest