class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m = len(word1)
        n = len(word2)
        length = min(m,n)
        res=""
        for i in range(length):
            res+= word1[i]+word2[i]
        res+=word1[length:]
        res+=word2[length:]
        return res

        