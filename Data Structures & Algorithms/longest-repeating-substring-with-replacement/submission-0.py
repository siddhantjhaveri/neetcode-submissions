class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        maxfreq = 0
        maxlen = 0
        
        for right in range(len(s)):
            char = s[right]
            count[char] = count.get(char, 0) + 1
            maxfreq = max(maxfreq, count[char])
            
            # If window invalid, shrink from left
            while (right - left + 1) - maxfreq > k:
                left_char = s[left]
                count[left_char] -= 1
                left += 1
            
            maxlen = max(maxlen, right - left + 1)
        
        return maxlen
