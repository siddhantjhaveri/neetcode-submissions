class Solution:
    
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        print('String to decode: ', s)
        res = []
        i = 0
        while i < len(s):
            print('pointer i at: ' ,i)
            j = i
            while s[j] != '#':
                print(f'iterating through s[j] which is at s[{j}] = {s[j]}')
                j += 1
            length = int(s[i:j])
            print('Get length of string to be decoded: ', length)
            i = j + 1
            j = i + length
            res.append(s[i:j])
            print('decoded word: ', s[i:j])
            i = j
            
        return res