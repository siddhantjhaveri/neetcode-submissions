class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n
        
        # Pass 1: Left to Right
        left_product = 1
        for i in range(n):
            result[i] = left_product
            left_product *= nums[i]
        print(result)
        # Pass 2: Right to Left
        right_product = 1
        for i in range(n - 1, -1, -1):
            result[i] *= right_product
            right_product *= nums[i]
        
        return result


        