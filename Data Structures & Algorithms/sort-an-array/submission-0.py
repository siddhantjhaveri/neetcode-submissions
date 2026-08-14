class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge_sort(nums):
            if len(nums)<=1:
                return nums
            mid = len(nums)//2
            left = nums[:mid]
            right = nums[mid:]
            # Recursively split both halves until they're single elements
            left_sorted = merge_sort(left)
            right_sorted = merge_sort(right)
            
            return merge(left_sorted,right_sorted)
        def merge(left,right):
            res = []
            i,j = 0,0
            while i<len(left) and j<len(right):
                if left[i]<right[j]:
                    res.append(left[i])
                    i+=1
                else:
                    res.append(right[j])
                    j+=1
            res.extend(left[i:])
            res.extend(right[j:])
            return res
        return merge_sort(nums)

        