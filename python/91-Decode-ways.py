#best solution - iterative bottom up
class Solution:
    def numDecodings(self, s: str) -> int:
        first, second=0,1

        for i in range(len(s)):
            temp_sum=0
            if int(s[i]) >0 and int(s[i])<=9:
                temp_sum+=second
            if i>0 and int(s[i-1:i+1]) >=10 and int(s[i-1:i+1])<=26:
                temp_sum+=first
            first=second
            second=temp_sum
        return second


class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
    
        first = 1
        second = 1
        for i in range(1, len(s)):
            current = 0
            if s[i] != "0":
                current = second
            two_digit = int(s[i - 1: i + 1])
            if two_digit >= 10 and two_digit <= 26:
                current += first
            first = second
            second = current
        
        return second