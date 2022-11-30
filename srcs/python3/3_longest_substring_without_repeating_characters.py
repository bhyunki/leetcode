class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last = {}
        m = 0
        left = 0
        for i, c in enumerate(s):
            if c in last and left <= last[c]:
                left = last[c] + 1 # substring cannot contain repeated char
            else:
                m = max(m, i - left +1)
            
            last[c] = i
        return m
