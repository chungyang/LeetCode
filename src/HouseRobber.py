class HouseRobber:
    def rob(self, nums):
        
        if not nums:
            return 0
        
        max_money = [0,nums[0]]
        
        for i in range(1,len(nums)):
            max_money.append(max(max_money[i], nums[i] + max_money[i - 1]))
            
        return max(max_money[len(max_money) - 1], max_money[len(max_money) - 2])
        """
        :type nums: List[int]
        :rtype: int
        """