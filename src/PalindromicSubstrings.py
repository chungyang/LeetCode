#Given a string, your task is to count how many palindromic substrings in this string.
#The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

#Example
#Input: "abc"
#Output: 3
#Explanation: Three palindromic strings: "a", "b", "c".
#

import math
class PalindromicSubstrings:
    def countSubstrings(self, S):
        N = len(S)
        ans = 0
        for center in range(2*N - 1):
            left = math.floor(center / 2)
            right = left + center % 2
            while left >= 0 and right < N and S[left] == S[right]:
                ans += 1
                left -= 1
                right += 1
        return ans