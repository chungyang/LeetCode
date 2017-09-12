//Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
//Example:
//Input: "babad"
//Output: "bab"
//Note: "aba" is also a valid answer.
//Example:
//Input: "cbbd"
//Output: "bb"

public class LongestPalindrome {

	public static String longestPalindrome(String s) {

		if(s.isEmpty()){
			return "";
		}
		else if(s.length() == 1){
			return s;
		}

		int nPalindromeCenter = 2 * s.length();
		int longestLength = 0;
		String longestPalindrome = null;

		for(int center = 1; center < nPalindromeCenter - 1; center++){

			int left = (int) Math.ceil(center / 2.0) - 1;
			int right = center % 2 == 0? left + 1 : left;
			int palindromeLength = 0;

			while((left >= 0 && right < s.length()) && s.charAt(left) == s.charAt(right)){

				palindromeLength = right - left + 1;
				if(palindromeLength > longestLength){
					longestLength = palindromeLength;
					longestPalindrome = s.substring(left,right + 1);
				}
				left--;
				right++;
			}

		}

		return longestPalindrome;
	}
}
