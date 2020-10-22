import timeit


def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped


def multiple_append_operations(n):
    A = []
    for i in range(n):
        A.append(i)


def comprehension_append(n):
    A = [i for i in range(n)]


n = 100000
append_operation_wrapper = wrapper(multiple_append_operations, n)
comprehension_wrapper = wrapper(comprehension_append, n)

timeit_append = timeit.timeit(append_operation_wrapper, number=100)
comprehension_timeit = timeit.timeit(comprehension_wrapper, number=100)

print("timeit_append  : ", timeit_append)
print("timeit_append  : ", comprehension_timeit)