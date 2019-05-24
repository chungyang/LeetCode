class Solution {
    public List<Integer> findDuplicates(int[] nums) {
        
        List<Integer> solution = new ArrayList<Integer>();
        
        
        for(int i = 0; i < nums.length; i++){
            
            int num = nums[i];
            
            if(nums[Math.abs(num) - 1] < 0){
                solution.add(Math.abs(num));
            }
            else{
                nums[Math.abs(num) - 1] *= -1;
            }
        }
        
        return solution;
    }
}