class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        r=len(heights)-1
        max_a = 0
        while l<r:
            length = min(heights[l],heights[r])
            breadth = r-l
            max_a = max(max_a, length*breadth)
            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
        return max_a

        
        