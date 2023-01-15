import math
import os
import random
import re
import sys

def matrix_script(matrix, n, m, list_of_alphanumeric):
    new_string = ''
    for i in range(m):
        for j in range(n):
            count = 0
            while count == 0 and j != 0 and matrix[j][i] not in list_of_alphanumeric and matrix[j-1][i] in list_of_alphanumeric:
                new_string = new_string + ' '
                count = 1
            
            count_new = 0
            while matrix[j][i] in list_of_alphanumeric and count_new==0:
                new_string = new_string + matrix[j][i]
                count_new = 1
    add_string = ''
    for i in range(n):
        count_b = 0
        while matrix[n-1-i][m-1] not in list_of_alphanumeric and count_b == 0:
            add_string = matrix[n-1-i][m-1] + add_string
            count_b = 1
    new_string = new_string + add_string
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
