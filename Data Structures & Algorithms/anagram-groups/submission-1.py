class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a = defaultdict(list)
        for i in strs:
            b = ''.join(sorted(i))
            a[b].append(i)
        return(list(a.values()))