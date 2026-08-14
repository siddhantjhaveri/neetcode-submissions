class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        l,r =0, len(arr)-1
        new_arr = []
        for i in range(len(arr)-1):
            if i == len(arr)-1:
                arr.append(-1)
                break
            max_val = 0
            while l<r:
                max_val = max(arr[r], max_val)
                r-=1
            new_arr.append(max_val)
            l+=1
            r=len(arr)-1
        new_arr.append(-1)
        return new_arr


        