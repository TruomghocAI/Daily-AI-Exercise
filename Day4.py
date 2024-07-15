def convolve_2d(input_matrix, kernel):
    # Kích thước ma trận đầu vào
    input_height = len(input_matrix)
    input_width = len(input_matrix[0])
    
    # Kích thước kernel
    kernel_height = len(kernel)
    kernel_width = len(kernel[0])
    
    # Kích thước ma trận đầu ra
    output_height = input_height - kernel_height + 1
    output_width = input_width - kernel_width + 1
    
    # Khởi tạo ma trận đầu ra
    result = [[0 for _ in range(output_width)] for _ in range(output_height)]
    
    # Thực hiện tích chập
    for i in range(output_height):
        for j in range(output_width):
            sum = 0
            for ki in range(kernel_height):
                for kj in range(kernel_width):
                    sum += input_matrix[i+ki][j+kj] * kernel[ki][kj]
            result[i][j] = sum
    
    return result

if __name__ == '__main__':
    A = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
    B = [[2, 4],[1, 3]]
    C = [[1,1,1],[0,0,0],[1,1,1]]