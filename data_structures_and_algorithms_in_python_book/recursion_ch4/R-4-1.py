"""
Describe a recursive algorithm for finding the maximum element in a se-
quence, S, of n elements. What is your running time and space usage?
"""
def max_element(s):
    def merge_sort(s):
        def merge(s1, s2, s):
            i = j = 0
            while i + j < len(s):
                if j == len(s2) or (i < len(s1) and s1[i] < s2[j]):
                    s[i + j] = s1[i]
                    i += 1
                else:
                    s[i + j] = s2[j]
                    j += 1

        def divide(s):
            n = len(s)
            if n < 2:
                return s
            mid = len(s) // 2
            s1 = s[0:mid]
            s2 = s[mid:n]

            merge_sort(s1)
            merge_sort(s2)

            merge(s1, s2, s)

        divide(s)
    merge_sort(s)
    return s[-1]

print(max_element([4,3,2,1]))
