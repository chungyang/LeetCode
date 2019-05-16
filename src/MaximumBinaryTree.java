/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public TreeNode constructMaximumBinaryTree(int[] nums) {
        
        if(nums.length == 0) {
			return null;
		}
		
		if(nums.length == 1){
			TreeNode root = new TreeNode(nums[0]);
			return root;
		}

		int maxIndex = 0;
		int maxNum = 0;

		for(int i = 0; i < nums.length; i++){

			if(nums[i] > maxNum){
				maxIndex = i;
				maxNum = nums[i];
			}
		}

		TreeNode root = new TreeNode(maxNum);
		root.left = constructMaximumBinaryTree(Arrays.copyOfRange(nums, 0, maxIndex));
		root.right = constructMaximumBinaryTree(Arrays.copyOfRange(nums, maxIndex + 1, nums.length));

		return root;
	}
        
}