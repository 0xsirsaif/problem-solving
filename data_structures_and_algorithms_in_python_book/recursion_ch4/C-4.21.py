"""
Suppose you are given an n-element sequence, S, containing distinct in-
tegers that are listed in increasing order. Given a number k, describe a
recursive algorithm to find two integers in S that sum to k, if such a pair
exists. What is the running time of your algorithm?
"""

def find_two_num(s, k):
    def binary_search(start, end, target):
        while end - start >= 1:
            mid = (start+end)//2
            if target == s[mid]:
                return (k-target, s[mid])
            elif target > s[mid]:
                return binary_search(mid+1, end, target)
            else:
                return binary_search(start, mid, target)
    for i in s:
        res = binary_search(0, len(s) - 1, k - i)
        if res:
            return res

print(find_two_num([-30,-2,-1,0,5,9,44,55,211], 8))