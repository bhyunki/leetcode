class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l=[]
        r=[]
        
        for i in range(len(nums)):
            l.append(0)
            r.append(0)
            
        l[0]=1
        for i in range(1, len(nums)):
            l[i] = l[i-1]*nums[i-1]

        r[len(nums)-1]=1
        for i in range(len(nums)-2, -1, -1):
            r[i] = r[i+1]*nums[i+1]
        
        answer=[]
        for i in range(len(nums)):
            answer.append(l[i]*r[i])

        return answer
