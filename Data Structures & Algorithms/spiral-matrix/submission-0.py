class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # repeat this whole step
        # first start go right as much as possible
        # then go down as much possible
        # then left as much possiible
        # then go up as much as possible as long dont hit visitied 

        res = []
        left, right, = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        while left < right and top < bottom:
            # get every value in top row
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1

            # next get every i in right col
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            right -= 1
            if not (left < right and top < bottom):
                break
            # get every i in bottom col

            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1

            # for every i inbetween bottom and top
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
        
        return res
