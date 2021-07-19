class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        if len(nums) < 3:
            return []
        
        s=sorted(nums)
        l=[]
        
        for i in range(len(s)):
            if i > 0 and s[i] == s[i-1]:
                continue
            left = i+1
            right = len(s)-1
        
            while left < right:
                t = s[i] + s[left] + s[right] 
                if t == 0:
                    l.append([s[i], s[left], s[right]])
                    while left < right and s[left] == s[left+1]:
                        left+=1
                    while left < right and s[right] == s[right-1]:
                        right-=1
                    left+=1
                    right-=1
                    
                elif t < 0:
                    left += 1
                elif t > 0:
                    right -= 1
        return l
