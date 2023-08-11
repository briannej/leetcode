class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        up,down= 0, rows-1
        while up<=down:
            mid = up + (down-up)//2
            if target < matrix[mid][0]:
                down = mid-1
            elif target> matrix[mid][-1]:
                up = mid+1
            else:
                break
        l,r = 0, cols-1
        while l<=r:
            m = l+(r-l)//2
            if target == matrix[mid][m]:
                return True
            elif target > matrix[mid][m]:
                l= m+1
            else:
                r=m-1
        return False