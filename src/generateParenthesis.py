class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        
        def backtracking(s = '',left = 0, right = 0):
            
            if len(s) == 2*n:
                ans.append(s)
                return
            
            if left < n:
                backtracking(s+'(', left+1, right)
            if right < left:
                backtracking(s+')',left, right+1)
        
        
        backtracking()
        return ans
            