class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        
        counts = {}
        left = 0
        res = 0
        max_freq = 0
        for right in range(len(s)):
           #need freq check to detect which to change
           char = s[right]
           counts[char] = counts.get(char, 0) + 1
           max_freq = max(max_freq, counts[char])

           window_size = right - left + 1

           while window_size-max_freq > k:
            counts[s[left]] -= 1
            left += 1
            window_size = right - left + 1

        res = max(res, window_size)

        return res




