class rotate_matrix_on_90:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        if mat == target:
            return True
        if mat[::-1] == target:
            return True
        else:
            def rotate_90(matrix):
                n = len(matrix)
                rotated = [[0] * n for _ in range(n)]
                for i in range(n):
                    for j in range(n):
                        rotated[j][n - 1 - i] = matrix[i][j]
                return rotated
            def is_equal(matrix1, matrix2):
                return all(
                    matrix1[i][j] == matrix2[i][j]
                    for i in range(len(matrix1))
                    for j in range(len(matrix1[0]))
                )

            if is_equal(mat, target):
                return True
            current_mat = mat
            for _ in range(3):
                current_mat = rotate_90(current_mat)
                if is_equal(current_mat, target):
                    return True
            return False
