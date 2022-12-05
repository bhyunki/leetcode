class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        results=[]
        d = {'2':"abc", '3':"def", '4':"ghi", '5':"jkl", '6':"mno", '7':"pqrs", '8':"tuv", '9':"wxyz"}
        def dfs(index:int, s:string):
            if len(s) == len(digits):
                results.append(s)
                return

            for c in d[digits[i]]:
                dfs(i+1, s+c)

            return

        if not digits:
            return []

        dfs(0, "")
        return  results
