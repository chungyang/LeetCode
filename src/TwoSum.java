//Given an array of integers, return indices of the two numbers such that they add up to a specific target.
//You may assume that each input would have exactly one solution, and you may not use the same element twice.
public class TwoSum {

	public static int[] twoSum(int[] nums, int target) {

		int[] answers = new int[2];

		if(nums.length < 2){
			return answers;
		}

		for(int i = 0; i < nums.length; i++){

			int remainder = target - nums[i];

			for(int j = i + 1; j < nums.length; j++){
				if(remainder - nums[j] == 0){

					answers[0] = i;
					answers[1] = j;
					return answers;
				}
			}
		}
		return answers;
	}

	public static void main(String[] args){

		int[] nums = {9,3,20,12,7};
		int[] answers = twoSum(nums,12);
		System.out.println(answers[0] + " " + answers[1]);
	}
}

