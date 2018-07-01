class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == None:
            return True
        
        if len(s) == 1:
            return False
        
        stack = []
        push_action = {"(", "[", "{"}
        pop_action = {")":"(", "]":"[", "}":"{"}
        
        for c in s:
            
            if c in push_action:
                stack.append(c)
            
            elif c in pop_action and len(stack) > 0:
                temp = stack.pop()
                
                if not temp == pop_action[c]:
                    return False
            elif c in pop_action and len(stack) == 0:
                return False
        
        if len(stack) > 0:
            return False
        
        return True