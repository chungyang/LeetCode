class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        countmap = {}
        
        for num in nums:
            
            if num in countmap:
                countmap[num] += 1
            else:
                countmap[num] = 1
        
        max_count = -1
        majority_element = -1
        
        for key in countmap.keys():
            
            if max_count < countmap[key]:
                max_count = countmap[key]
                majority_element = key
                
        return majority_element