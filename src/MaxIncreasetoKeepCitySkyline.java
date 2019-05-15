class Solution {
    public int maxIncreaseKeepingSkyline(int[][] grid) {
        
        int[] rowMaxNumbers = new int[grid.length];
        int[] colMaxNumbers = new int[grid[0].length];
        
        int total = 0;
        for(int i = 0; i < grid.length; i++){
            
            int rowMaxNumber = 0;
            for(int j = 0; j < grid[0].length; j++){
                
                if(grid[i][j] > rowMaxNumber){
                    rowMaxNumber = grid[i][j];
                }
                
                if(grid[i][j] > colMaxNumbers[j]){
                    colMaxNumbers[j] = grid[i][j];
                }
            }
            
            rowMaxNumbers[i] = rowMaxNumber;
        }
        
        for(int i = 0; i < rowMaxNumbers.length; i++){
            for(int j = 0; j < colMaxNumbers.length; j++){
                total += Math.min(rowMaxNumbers[i], colMaxNumbers[j]) - grid[i][j];
            }
        }
        
        return total;
    }
}