class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.mat = matrix
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        tsum = 0
        for row in range(len(self.mat)):
            for col in range(len(self.mat[row])):
                if row1<= row <=row2 and col1<= col <=col2:
                    tsum+= self.mat[row][col]
        return tsum
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)