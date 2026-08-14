class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Dictionary to store how many times a prefix sum has appeared
        prefix_count = defaultdict(int)
        
        # Initial state: a sum of 0 happens once (empty subarray)
        prefix_count[0] = 1
        
        current_sum = 0
        result = 0
        
        for num in nums:
            # Add the current number to our running total
            current_sum += num
            
            # We need to find if (current_sum - k) happened before
            target = current_sum - k
            
            # If it did, every occurrence forms a valid subarray ending here
            if target in prefix_count:
                result += prefix_count[target]
            
            # Record that we have seen this current_sum
            prefix_count[current_sum] += 1
            
        return result
        