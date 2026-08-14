class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ct, ft = 0,0
        res = []
        while ct<len(temperatures):
            temp = temperatures[ct]
            c = 0
            while temp>=temperatures[ft]:
                c+=1
                ft+=1
                if ft==len(temperatures):
                    c=0
                    break
            res.append(c)
            ct+=1
            ft=ct
        return res