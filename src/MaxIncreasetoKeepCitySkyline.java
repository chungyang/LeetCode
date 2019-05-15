class Solution {
    public int maxIncreaseKeepingSkyline(int[][] grid) {
        
        int[] rowMaxNumbers = new int[grid.length];
        int[] colMaxNumbers = new int[grid[0].length];
        
        for(int i = 0; i < grid.length; i++){
            
            for(int j = 0; j < grid[0].length; j++){
                rowMaxNumbers[i] = Math.max(rowMaxNumbers[i], grid[i][j]);
                colMaxNumbers[j] = Math.max(colMaxNumbers[j], grid[i][j]);
            }
            
        }
        
        int total = 0;
        for(int i = 0; i < rowMaxNumbers.length; i++){
            for(int j = 0; j < colMaxNumbers.length; j++){
                total += Math.min(rowMaxNumbers[i], colMaxNumbers[j]) - grid[i][j];
            }
        }
        
        return total;
    }
}