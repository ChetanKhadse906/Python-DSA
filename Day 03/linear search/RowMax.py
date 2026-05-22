Matrix=[
    [100, 198, 333, 323],
    [122, 232, 221, 111],
    [223, 565, 245, 764]
    ]

for i in range(0, len(Matrix)):
    max=Matrix[i][0]
    for j in range(0, len(Matrix)):
        if Matrix[i][j]>max:
            max=Matrix[i][j]
    print(max)
