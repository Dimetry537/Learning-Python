def matrix_multiplication(first_matrix, second_matrix):
    if len(first_matrix[0]) != len(second_matrix):
        return False
    
    rows_size = len(first_matrix[0])
    cols_size = len(first_matrix)
    
    result_matrix = []

    for i in range(cols_size):
        result_matrix.append([0] * cols_size)
    
    for i in range(cols_size):
        for j in range(cols_size):
            for k in range(rows_size):
                result_matrix[i][j] += first_matrix[i][k] * second_matrix[k][j]

    return result_matrix

def test_identity():
    matrix = [[1, 2], [1, 2]]
    identity_matrix =[[1, 0], [0, 1]]
    result = matrix_multiplication(matrix, identity_matrix)

    assert result == matrix, "Identity matrix doesn't work"

def test_zero():
    matrix = [[1, 2], [1, 2]]
    zero_matrix = [[0, 0], [0, 0]]
    result = matrix_multiplication(matrix, zero_matrix)

    assert result == [[0, 0], [0, 0]], "Zero matrix doesn't work"

def test_full():
    first_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    second_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    result = matrix_multiplication(first_matrix, second_matrix)

    assert result == [[30, 36, 42], [66, 81, 96], [102, 126, 150]], "Matrix multiplication doesn't work"

def test_full_different_size():
    first_matrix = [[-5, -2, 1], [4, 6, 10]]
    second_matrix = [[7, 8], [-8, -12], [1, 2]]
    result = matrix_multiplication(first_matrix, second_matrix)
    print(result)
    assert result ==  [[-18, -14], [-10, -20]], "Matrix multiplication doesn't work"

def test_fail():
    first_matrix = [[-5, -2, 1], [4, 6, 10], [16, 24, 36]]
    second_matrix = [[7, 8], [-8, -12]]
    result = matrix_multiplication(first_matrix, second_matrix)
    assert result == False, "It doesn't respect invlid cases"

test_identity()
test_zero()
test_full()
test_fail()
test_full_different_size()
print("tests pass!")