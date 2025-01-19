n = 24
lst = [[-1 for i in range(n)] for i in range(n)]
for i in range(n):
    for j in range(n):
        smallest = 0;
        bads = []
        for k in range(0, i):
            if (lst[k][j] not in bads):
                bads.append(lst[k][j])
        for m in range (0,j):
            if (lst[i][m] not in bads):
                bads.append(lst[i][m])
        while smallest in bads:
            smallest += 1
        lst[i][j] = smallest

s = [[str(e) for e in row] for row in lst]
lens = [max(map(len, col)) for col in zip(*s)]
fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
table = [fmt.format(*row) for row in s]
print('\n'.join(table))


