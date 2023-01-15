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
            while n!= 0 and n != n and matrix[j][i] not in list_of_alphanumeric and matrix[j-1][i] in list_of_alphanumeric and matrix[j+1][i] in list_of_alphanumeric and count == 0:
                new_string = new_string + ' '
                count = 1
            while matrix[j][i] in list_of_alphanumeric and count==0:
                new_string = new_string + matrix[j][i]
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
