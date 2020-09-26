"""
Write a recursive function that will output all the subsets of a set of n
elements (without repeating any subsets).
# section 4.4
"""


def puzzle_solve(k, s, u):
    for i in u:
        s.append(i)
        u.remove(i)
        if k == 1:
            print(s)
        else:
            puzzle_solve(k - 1, s, u)
        s.remove(i)
        u.add(i)

# puzzle_solve(3, [], {'a', 'b', 'c'})


import itertools
def findsubsets(S,m):
    return set(itertools.combinations(S, m))
print(findsubsets({'a', 'b', 'c'}, 2))