def brute_force(a, b):
    i = 0
    j = 0
    k = 0

    _len3 = len(a[i][j])
    _len2 = len(a[i])
    _len1 = len(a)
    res = [[[0 for k in range(_len3)] for j in range(_len2)] for i in range(_len1)]

    while i < _len1:
        res[i][j][k] = a[i][j][k] + b[i][j][k]
        k += 1
        if k == _len3:
            j += 1
            k = 0
        elif j+1 == _len2:
            res[i][j][k] = a[i][j][k] + b[i][j][k]
            i +=1
            j = 0
            k = 0

    return res


A = [
    [
        [10,1],
        [1,1],
        [1,1],
        [1,1],
        [1,1]
    ],
    [
        [1,1],
        [1,1],
        [1,1],
        [1,1],
        [1,1]
    ],
    [
        [1,1],
        [1,1],
        [1,1],
        [1,100],
        [1,1]
    ],
    [
        [1,1],
        [1,1],
        [1,1],
        [1502,1],
        [1,1]
    ]
]
B = [
    [
        [15,1],
        [1,1],
        [1,1],
        [1,150],
        [1,1]
    ],
    [
        [1,1],
        [1,1],
        [1,1],
        [1,1],
        [1,1]
    ],
    [
        [1,1],
        [1,1],
        [1,1],
        [1,1],
        [1,1]
    ],
    [
        [1,1],
        [1,1],
        [1,1],
        [1,1],
        [1,1]
    ]
]

print(brute_force(A, B))