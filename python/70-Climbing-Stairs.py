class Solution:
    def climbStairs(self, n: int) -> int:
        first, second= 0,1
        for i in range(n):
            first, second= second, first+second
        return second
    
class Solution:
    def climbStairs(self, n: int) -> int:
        hashmap={-1:0,0:1}
        def helper(n):
            if n not in hashmap:
                hashmap[n]=helper(n-1)+helper(n-2)
            return hashmap[n]
        return helper(n)


class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        n1, n2 = 2, 3

        for i in range(4, n + 1):
            temp = n1 + n2
            n1 = n2
            n2 = temp
        return n2
