class MyCircularDeque:
    def __init__(self, k):
        self._data = [None] * k
        self._capacity = k
        self._size = 0
        self._front = 0

    def insertLast(self, element):
        if self._size == len(self._data):
            return False

        end = (self._front + self._size) % len(self._data)
        self._data[end] = element
        self._size += 1
        return True

    def deleteFront(self):
        if self.isEmpty():
            return False

        self._data[self._front] = None
        self._size -= 1
        self._front = (self._front + 1) % len(self._data)
        return True

    def insertFront(self, element):
        if self.isFull():
            return False

        # implement Right Shift
        self._front = (self._front - 1) % len(self._data)
        self._data[self._front] = element
        self._size += 1
        return True

    def deleteLast(self):
        if self.isEmpty():
            return False

        back = (self._front + self._size - 1) % len(self._data)
        self._data[back] = None
        self._size -= 1
        return True

    def getFront(self):
        if self.isEmpty():
            return -1
        return self._data[self._front]

    def getRear(self):
        if self.isEmpty():
            return -1
        back = (self._front + self._size - 1) % len(self._data)
        return self._data[back]

    def isEmpty(self):
        return self._size == 0

    def isFull(self):
        return self._size == self._capacity


circularDeque = MyCircularDeque(3)
print(circularDeque.insertLast(1))			# return true
print(circularDeque.insertLast(2))			# return true
print(circularDeque.insertFront(3))		    # return true
print(circularDeque.insertFront(4))		    # return false, the queue is full
print(circularDeque.getRear())  			# return 2
print(circularDeque.isFull())				# return true
print(circularDeque.deleteLast())			# return true
print(circularDeque.insertFront(4))		    # return true
print(circularDeque.getFront())			    # return 4


# Me =  [null,true,89,true,-1,true,true,true,true,false,true,false,19,true,45,45,true,true,82,true,98,true,99,82,82,82,99,99,true,8,8,8,8,true,true,75,true,true,true,59,59,59,false,true,true,22,true,None,22,false,false,true,75,true,74,true,21,true,true,None,false,63,63,true,true,76,76,true,true,None,true,26,26,26,67,true,false,36,36,true,true,true,true,87,None,87,true,85,true,true,false,None,None,None,None,true,None,false,true,true,true,true]
# Exp = [null,true,89,true,-1,true,true,true,true,false,true,false,19,true,45,45,true,true,82,true,98,true,99,82,82,82,99,99,true,8,8,8,8,true,true,75,true,true,true,59,59,59,false,true,true,22,true,98,22,false,false,true,75,true,74,true,21,true,true,74,false,63,63,true,true,76,76,true,true,74,true,26,26,26,67,true,false,36,36,true,true,true,true,87,74,87,true,85,true,true,false,74,74,74,74,true,74,false,true,true,true,true]