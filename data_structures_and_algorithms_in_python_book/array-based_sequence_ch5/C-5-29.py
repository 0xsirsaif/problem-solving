# running time of o(n), space complexity of o(n)
def natural_join(A, B):
    # running time of dict comprehension = o(1) ? temporary list
    # space complexity of dict comprehension = o(n)
    tree = {y: z for y, z in B}
    result = []
    # o(n)
    for x, y in A:
        z = tree.get(y) # o(1)
        if z is not None:
            result.append((x, y, z)) # o(1)* => o(n) for all n append operations

    return result


B = [(10,0), (1,0), (2,0), (3,0), (4,0), (5,0), (6,0), (7,0), (8,0), (9,0), (10,0)]
A = [(0,0), (1,1), (2,2), (3,3), (4,4), (5,5), (6,6), (7,7), (8,8), (9,9), (10,10)]
print(natural_join(A, B))