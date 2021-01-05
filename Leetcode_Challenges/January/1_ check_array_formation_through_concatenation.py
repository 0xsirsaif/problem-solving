from typing import List
from itertools import chain


class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        map = {x[0]: x for x in pieces}
        return list(chain(*[map.get(x, []) for x in arr])) == arr

