class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # numd = {}
        # for i in range(len(numbers)):
        #     num = target - numbers[i]
        #     if num not in numd:
        #         numd[numbers[i]] = i
        #     else:
        #         return [numd[num]+1,i+1]
        l=0
        r=len(numbers)-1
        while l<r:
            a = numbers[l]+numbers[r]
            if a>target:
                r-=1
            elif a<target:
                l+=1
            else:
                return [l+1,r+1]

        