#Given n non-negative integers a1, a2, ..., an, where each r
#epresents a point at coordinate (i, ai). n vertical lines are 
#drawn such that the two endpoints of line i is at (i, ai) and (i, 0). 
#Find two lines, which together with x-axis forms a container, such that the container contains the most water.

#Note: You may not slant the container and n is at least 2.

#!/usr/bin/python
class Solution(object):
    def maxArea(self,height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        maxarea = 0
        
        while(left != right):

            left_height = height[left]
            right_height = height[right]

            maxarea = max(maxarea, min(left_height,right_height) * (right - left))

            if(left_height >= right_height):
                right = right - 1
            elif(left_height < right_height):
                left = left + 1

        return maxarea
