class UniquePaths:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        
        solution = []
        
        #initialize 2D list
        
        for x in range(0,m):
            solution.append([])
            for y in range(0,n):
                solution[x].append(0)
  
        for x in range(0,m):
            for y in range(0,n):
                
                if x == 0 or y == 0:
                    solution[x][y] = 1
                else:
                    solution[x][y] = solution[x - 1][y] + solution[x][y - 1]
                    
        
        return solution[m - 1][n - 1]