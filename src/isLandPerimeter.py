class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        perimeter = 0
        
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                
                
                if grid[y][x] == 1:
                    
                    if x == 0:
                        perimeter += 1
                    if x == len(grid[y]) - 1:
                        perimeter += 1
         
                        
                    if y == 0:
                        perimeter += 1
                    if y == len(grid) - 1:
                        perimeter += 1
                    
                    if (y - 1) >= 0 and grid[y - 1][x] == 0:
                        perimeter += 1
                    if (y + 1) < len(grid) and grid[y + 1][x] == 0:
                        perimeter += 1
                    if (x - 1) >= 0 and grid[y][x - 1] == 0:
                        perimeter += 1
                    if (x + 1) < len(grid[y]) and grid[y][x + 1] == 0:
                        perimeter += 1
                        
        return perimeter