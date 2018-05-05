class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        permutations = []
        
        self.permute_helper([],nums,permutations)
        
        return permutations
    
    
    def permute_helper(self,prefix, body, permutation):
        
        if len(body) == 1:
            merged_list = prefix + body
            permutation.append(merged_list)
            return
        
        for i in range(len(body)):
            self.permute_helper(prefix + [body[i]], body[0:i] + body[i+1:], permutation)     