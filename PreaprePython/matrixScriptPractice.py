import math
import os
import random
import re
import sys

def matrix_script(matrix, n, m, list_of_alphanumeric):
    matrix_string = []
    alpha_numeric_index = []
    new_string = ''
    for i in range(m):
        for j in range(n):
            count = 0
            while matrix[j][i] in list_of_alphanumeric and count == 0:
                alpha_numeric_index.append(len(matrix_string))
                count = 1
            matrix_string.append(matrix[j][i])

    

    for i in range(len(matrix_string)-1):
        count = 0 
        while i> int(alpha_numeric_index[-1]) and count == 0:
            new_string = new_string + matrix_string[i]
            count = 1
        while i< int(alpha_numeric_index[0]) and count == 0:
            new_string = new_string + matrix_string[i]
            count = 1
        while matrix_string[i] not in list_of_alphanumeric and matrix_string[i-1] in list_of_alphanumeric and count == 0 and int(alpha_numeric_index[0]<i<int(alpha_numeric_index[-1])):
            new_string = new_string + " "
            count = 1
        while count == 0 and matrix_string[i] in list_of_alphanumeric:
            new_string = new_string + matrix_string[i]
            count = 1
        
    return print(new_string)

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    matrix = []
    list_of_alphanumeric = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    for _ in range(n):
        matrix_item = input()
        matrix.append(matrix_item)
    matrix_script(matrix, n, m, list_of_alphanumeric)
