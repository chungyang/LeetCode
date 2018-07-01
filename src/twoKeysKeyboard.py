# No.650
class Solution:
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 0
    
        solution = [0,1,2]
    
        for i in range(3,n + 1):
            
            is_prime = True
            solution.append(0)
            
            if i % 2 == 0:
                solution[i] = solution[int(i/2)] + 2
                is_prime = False
                continue
            
            for j in range(3,int(i/2),2):
                
                if i % j == 0:
                    solution[i] = i / j + solution[j] 
                    is_prime = False
                    continue
            
            if is_prime:
                solution[i] = i
                    
        return int(solution[n])