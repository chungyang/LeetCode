class Solution:
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        
        for i in range(1,len(nums),2):
            
            if i+1 >= len(nums):
                return
            temp = nums[i]
            
            nums[i] = nums[i+1]
            nums[i+1] = temp