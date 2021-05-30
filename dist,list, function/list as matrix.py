# NUM_ROWS = 25
# NUM_COLS = 25
#
#
# def trace(matrix):
#     sum = 0
#     n = len(matrix)
#     for i in range(n):
#         for j in range(n):
#             if j == i:
#                 sum += matrix[i][j]
#     return sum
#
#
# my_matrix = []
# for row in range(NUM_ROWS):
#     new_row = []
#     for col in range(NUM_COLS):
#         new_row.append(row * col)
#     my_matrix.append(new_row)
#
# # print the matrix
# for row in my_matrix:
#     print(row)
#
# print(trace(my_matrix))

NUM_ROWS = 5
NUM_COLS = 9

# construct a matrix
my_matrix = {}
for row in range(NUM_ROWS):
    row_dict = {}
    for col in range(NUM_COLS):
        row_dict[col] = row * col
    my_matrix[row] = row_dict

for key,value in my_matrix.items():
    print(key,value)

# print the matrix
for row in range(NUM_ROWS):
    for col in range(NUM_COLS):
        print(my_matrix[row][col], end=" ")
    print()