class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def calcHours(k):
            sum=0
            for pile in piles:
                sum += math.ceil(pile/k)
            return sum


        l,r =1, max(piles)
        answer=r
        while l<=r:
            m= l+(r-l)//2
            if calcHours(m) > h:
                l=m+1
            else:
                answer=m
                r=m-1
        return answer
