import math

class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return -1
        
        character_map = {}
        
        for c in s:
            
            if c in character_map:
                character_map[c] += 1
            else:
                character_map[c] = 1

        ans = math.inf
        
        for k in character_map:
            
            if character_map[k] == 1:
                ans = min(s.find(k),ans)
            
        return -1 if ans is math.inf else ans