from main import Matrix

data = Matrix((5, 5), dtype=float)

data[0][1] = 1
data[2][3] = 2
data[4, 2] = 0.12312312313312213

print(data)

data.columns -= 1

print(data.to_tuple())
