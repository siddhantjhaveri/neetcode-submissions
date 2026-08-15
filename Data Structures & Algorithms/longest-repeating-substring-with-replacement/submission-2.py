class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0] * 26
        left = 0
        max_freq = 0
        max_len = 0
        
        for right in range(len(s)):
            # Add new character
            count[ord(s[right]) - ord('A')] += 1
            max_freq = max(max_freq, count[ord(s[right]) - ord('A')])
            
            # If window is invalid, shrink from left
            window_len = right - left + 1
            if window_len - max_freq > k:
                count[ord(s[left]) - ord('A')] -= 1
                left += 1
                # Note: max_freq might not be accurate now, but it's okay!
                # We only need it to be an upper bound. It can be slightly higher.
            
            # Update max length
            max_len = max(max_len, right - left + 1)
        
        return max_len
