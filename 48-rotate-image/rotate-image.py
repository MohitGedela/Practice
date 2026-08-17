class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(i+1, len(matrix)):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp

        for row in matrix:
            left = 0
            right = len(row) - 1

            while left < right:
                temp = row[left]
                row[left] = row[right]
                row[right] = temp

                left += 1
                right -= 1