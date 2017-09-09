#Divide two integers without using multiplication, division and mod operator.
#If it is overflow, return MAX_INT.

#!/usr/bin/python
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1
            
        n_shift = 0
        quotient = 0
        
        dividend_abs = abs(dividend)
        divisor_abs = abs(divisor)
 
        while(dividend_abs >= divisor_abs):
        
            temp_divisor = divisor_abs
            n_shift = 0
            while(dividend_abs >= temp_divisor << 1):
                temp_divisor <<= 1
                n_shift += 1
            
            dividend_abs -= temp_divisor
            quotient += 2 ** n_shift
        
        quotient = quotient if (sign == 1) else -quotient
        return min(max(-2147483648,quotient),2147483647)