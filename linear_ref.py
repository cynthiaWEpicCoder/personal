# Matrices as Lists of Lists
# A simple introduction to handling matrices as lists of lists in Python
# Patrick Honner 9/21/22

# Need this to deepcopy lists
import copy

# Makes presenting a table of data easier
from tabulate import tabulate

# We'll hardcode the matrix as a list of lists
# The nested lists function as the rows of the matrix

row_1 = [3, -4, 0, 5]
row_2 = [-1, -2, 3, 10]
row_3 = [4, 1, 1, 3]

M = [ row_1, row_2, row_3]


def scale(row, scalar):
    # Convert the string input to a float
    scalar = float(scalar)
    # Perform the elementary row operation
    for i in range(len(M[row])):
        M[row][i]=scalar*M[row][i]

# A function to print out a list of lists, i.e. a matrix
# tabulate is nicer, so I didn't use this, but left as an example


def swap(rowA, rowB):
  temp = M[rowA]
  M[rowA] = M[rowB]
  M[rowB] = temp

def scale_add(scaleRow, fixedRow, scalar):
   for i in range(len(M[fixedRow])):
      M[fixedRow][i] += M[scaleRow][i] * scalar

k = 0
s = 0


def ref(matrix):
    m = len(matrix)  
    n = len(matrix[0]) 
    k = 0
    s = 0 
    while k < m and s < n:
        pivot_row = None
        for r in range(k, m):
            if matrix[r][s] != 0:
                pivot_row = r
                break
        if pivot_row is None:
            s += 1
            continue
        if pivot_row != k:
            swap(k, pivot_row)
        pivot_val = matrix[k][s]
        scale(k, 1 / pivot_val)
        for r in range(k + 1, m):
            if matrix[r][s] != 0:
                factor = -matrix[r][s]
                scale_add(k, r, factor)
        k += 1
        s += 1
    for i in range(m - 1):
        for j in range(m - 1 - i):
            if all(val == 0 for val in matrix[j]) and not all(val == 0 for val in matrix[j + 1]):
                swap(j, j + 1)
    return matrix

print(tabulate(ref(M)))