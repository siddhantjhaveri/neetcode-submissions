class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums)+1)]
        for i in nums:
            count[i] = count.get(i,0)+1
        for num, cnt in count.items():
            freq[cnt].append(num)
        res = []
        for j in range(len(freq)-1,0,-1):
            for item in freq[j]:
                if k>0:
                    res.append(item)
                    k-=1
        return res


        