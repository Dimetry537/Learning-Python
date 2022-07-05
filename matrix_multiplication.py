from matrices import first_matrix, second_matrix

def matrix_multiplication():
    
    lenght_matrix = len(first_matrix)
    
    result_matrix = []
    
    for i in range(lenght_matrix):
        result_matrix.append([0] * lenght_matrix)
    
    for i in range(lenght_matrix):
        for j in range(lenght_matrix):
            for k in range(lenght_matrix):
                result_matrix[i][j] += first_matrix[i][k] * second_matrix[k][j]
        
    print(result_matrix)
    return result_matrix
    
matrix_multiplication()