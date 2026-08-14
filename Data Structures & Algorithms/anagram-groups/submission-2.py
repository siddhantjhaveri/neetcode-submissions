class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for i in strs:
            cleaned = ''.join(sorted(i))
            res[cleaned].append(i)
        return list(res.values()) 
        