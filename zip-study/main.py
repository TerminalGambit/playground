matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix_columns = zip(*matrix)

for arr in matrix_columns:
    arr = list(arr)
    print(arr)
