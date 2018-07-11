class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        sol = 0
        
        for c in s:
            sol ^= ord(c)
        
        for c in t:
            sol ^= ord(c)
                 
        return chr(sol)