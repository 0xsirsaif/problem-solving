def last_doubling_operation(n):
    def nearest_value(append_ops):
        start = 0
        end = len(fixed_places)-1
        last_mid = None

        while start <= end:
            mid = last_mid = (start + end) // 2
            if fixed_places[mid] == append_ops:
                return mid
            if fixed_places[mid] > append_ops:
                end = mid - 1
            elif fixed_places[mid] < append_ops:
                start = mid + 1
        else:
            if fixed_places[last_mid] < n:
                return fixed_places[last_mid]
            else:
                return fixed_places[last_mid - 1]

    fixed_places = [2**x for x in range(100)]
    result = nearest_value(n)
    return result

print(last_doubling_operation(10))