class Solution:

    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        index_map = {}
        
        for i,b in enumerate(B):
            index_map[b] = i
        
     
        return [index_map[a] for a in A]