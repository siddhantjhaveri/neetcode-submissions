class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        # i marks the position of the last unique element we placed
        i = 0  
        
        # j is our scout, scanning from the second element onward
        for j in range(1, len(nums)):
            # If we find a new unique number
            if nums[j] != nums[i]:
                # Move the unique pointer forward
                i += 1
                # Place the new unique number right next to the others
                nums[i] = nums[j]
        
        # The number of unique elements is the index + 1
        return i + 1