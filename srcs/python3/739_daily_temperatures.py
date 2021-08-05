class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = []
        stack = []
        
        for i,t in enumerate(temperatures):
            ans.append(0)
            while stack and t > temperatures[stack[-1]]:
                last=stack.pop()
                ans[last]= i - last
            stack.append(i)
        
        return ans
