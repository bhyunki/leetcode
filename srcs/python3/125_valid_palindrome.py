class Solution:
    def isPalindrome(self, s: str) -> bool:
        answer=""
        for c in s:
            if c.isalpha() == True:
                answer+=c.lower()
            elif c.isdigit() == True:
                answer+=c
        if answer[::-1] == answer:
            return True
        return False
