A = [[1, 2], [3, 4]]  # 2by2 matrix

scalar = 2  # positive int


product = [[i*scalar for i in sublist] for sublist in A]

print(product)

for row in A:

    temp = []

    for element in row:
        temp.append(scalar * element)

    product.append(temp)

print(product)