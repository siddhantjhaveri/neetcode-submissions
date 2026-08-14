class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        r = min(len(word1),len(word2))
        s = ""
        for i in range(r):
            s+= word1[i] + word2[i]
        return s + word1[i+1:] + word2[i+1:]


        