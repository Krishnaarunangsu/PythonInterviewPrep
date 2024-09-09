Rows=int(input("Enter the number of rows:"))
Columns=int(input("Enter the number of columns:"))

# Initialize Matrix
matrix=[]
print("Enter the entries row wise:")

# For user input
# A loop for row entries
for row in range(Rows):
        a=[]
        # A loop for column entries
        for column in range(Columns):
                a.append(int(input()))
        matrix.append(a)

print(matrix)
# For prining the matrix
# for row in range(Rows):
#         for column in range(Columns):
#                 print(f'The matrix is:\n{matrix[row][column]}', end=" ")
#         print()

