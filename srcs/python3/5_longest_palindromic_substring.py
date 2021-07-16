class Solution:
    def longestPalindrome(self, s: str) -> str:
        l=[]
        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[i]==s[j]:
                    t = s[i:j+1]
                    if t == t[::-1]:
                        l.append(t)
        l.sort(key=len, reverse=True)
        return l[0]
