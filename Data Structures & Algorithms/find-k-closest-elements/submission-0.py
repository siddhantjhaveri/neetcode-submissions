class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l = 0
        r = len(arr)-1
        while r-l+1 > k:
            d_l = abs(arr[l]-x)
            d_r = abs(arr[r]-x)
            if d_l > d_r:
                l+=1
            else:
                r-=1
        return arr[l:r+1]      
            
        