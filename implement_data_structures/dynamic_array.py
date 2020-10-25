import ctypes

# TODO
# Shrinking array capacity after pop element

class DynamicArray:
    def __init__(self):
        # number of current items
        self._len = 0
        # the capacity of the array
        self._capacity = 1
        # construct low level array using ctype module by non public _make_low_level_arr method
        self._low_level_arr = self._make_low_level_arr(self._capacity)

    def __getitem__(self, item):
        # does not support negative indexing, yet
        if not 0 <= item < self._len:
            raise ImportError("Invalid Index")
        return self._low_level_arr[item]

    def append(self, obj):
        # if all available array cells are exhausted, we double array capacity
        # using private _resize method
        if self._len == self._capacity:
            self._resize(2 * self._capacity)
        # if there is a free cells, _curr_elements_num refers to the index next the last occupied one
        self._low_level_arr[self._len] = obj
        # after appending the obj, _curr_elements_num incremented by one
        self._len += 1

    def insert(self, idx, value):
        """insert at passed index"""
        # Doubling the array if it is full
        if self._len == self._capacity:
            self._resize(2 * self._capacity)
        # right shifting all the elements right to the desired index
        for i in range(self._len, idx, -1):
            self._low_level_arr[i] = self._low_level_arr[i - 1]
        # insert the value in the desired index
        self._low_level_arr[idx] = value
        # increase array length by 1
        self._len += 1

    def remove(self, value):
        """remove the first occurrence of passed element"""
        # loop until find the value
        for i in range(self._len):
            if self._low_level_arr[i] == value:
                # make use of the pop method for left-shifting elements
                self.pop(i)

    def pop(self, idx=None):
        # parametrized pop method
        index = self._len if idx is None else idx
        # left-shifting all elements to the removed elements, shifting = removing
        for i in range(index, self._len - 1):
            self._low_level_arr[i] = self._low_level_arr[i + 1]
        self._len -= 1

        # shrinking the array capacity after removing 3/4 of array elements
        if self._len == self._capacity//4:
            self._resize(self._capacity // 2)

    def extend(self, array):
        """
        extend method to add bunch of elements at the end of the array one time instead of calling append method
        many times, as we can compute the additional capacity we need, so we resizing the array once
        """
        arr_len = len(array)
        # resizing array by twice length of the additional array
        if self._len + arr_len >= self._capacity:
            self._resize(2 * arr_len)
        # cheap append operations after computing the needed size to resize the array once
        for i in array:
            self.append(i)

    def _resize(self, capacity):
        # _range = last element to add to the new array, in case of doubling => add all elements of old array,
        # in case of shrinking => add all elements to the (capacity//4)th index
        _range = self._capacity if capacity > self._capacity else self._capacity // 4
        # construct new low level array by private _make_low_level_arr method
        new_arr = self._make_low_level_arr(capacity)
        # assigning all values of old array to the new one
        for i in range(_range):
            new_arr[i] = self._low_level_arr[i]
        # reassign reference array to the new one
        self._low_level_arr = new_arr
        # reassign capacity
        self._capacity = capacity

    def _make_low_level_arr(self, capacity):
        return (capacity * ctypes.py_object)()

    def print_list(self):
        """return array elements in python list form, helping function for testing"""
        result = []
        for i in range(self._len):
            result.append(self._low_level_arr[i])
        return result

    def return_capacity_and_elements_num(self):
        return self._capacity, self._len

A = DynamicArray()
n = 50

for i in range(n):
    A.append(None)

print(A.return_capacity_and_elements_num())

for i in range(n):
    A.pop()

print(A.return_capacity_and_elements_num())
