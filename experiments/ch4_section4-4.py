# s = [0,1,2,3,4,5,6,7,8,9]

def linear_sum(s,n):
    if n == 0:
        return s[0]
    return linear_sum(s,n-1) + s[n]

# print(linear_sum(s,len(s)-1)

def reverse_seq(s, start, stop):
    if start < stop - 1:
        s[start], s[stop-1] = s[stop-1], s[start]
        return reverse_seq(s,start+1, stop-1)
    return s

# print(reverse_seq(s, 0, len(s)))


def puzzle_solve(k, s, u):
    for i in u:
        s.append(i)
        u.remove(i)
        if k == 1:
            print(s)
        else:
            puzzle_solve(k-1, s, u)
        s.remove(i)
        u.add(i)


s = {'a', 'b', 'c'}
for i in range(len(s)):
    print(puzzle_solve(i, [], s))