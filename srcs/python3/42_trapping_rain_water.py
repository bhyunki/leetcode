class Solution:
    def trap(self, height: List[int]) -> int:
        answer=0
        l=[]
        if len(height) == 0:
            return 0
        if max(height) == 0:
            return 0
        i=0
        m=0
        while True:
            if i >= len(height)-1:
                break

            if height[i]==0:
                i+=1
                continue
            
            m = height[i]
            if m > max(height[i+1:]):
                m = max(height[i+1:])
              
            for j in range(i+1, len(height)):
                if height[j] >= m:
                    i = j
                    break
                if height[j] < m:
                    answer += m-height[j]
            else:
                i+=1
            
        return answer
