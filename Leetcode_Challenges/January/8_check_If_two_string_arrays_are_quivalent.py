from typing import List
from itertools import zip_longest

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        """
        build both strings completely which requires O(N+M) space and time complexity,
        also we don't need to compare the whole elements if comparison fails -> time to lazy processing
        using generator
        """
        if len(word1) != len(word2):
            return False
        return ''.join(i for i in word1) == ''.join(j for j in word2)

    def Lazely_arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        """
        Two generators implicitly use pointers.
        yield Node -> to inform that if the iterable is exhausted then return None, if we don't write this statement,
        the zip() function will make an iterator of the len of the shortest word passed to it.

        if they are not the same len -> return False whenever the shortest one exhausted
        why we don't use zip directly without a generator -> let's take an example:
            one = ["A","BC"]
            two = ["AB", "C"]
            list(zip(one, two) => [("A","AB"), ("BC","C")] ? I hope you got it!
        """
        def _lazy_generator(word: List):
            """ two nested loops to inform that we are taking a single element/letter"""
            for i in word:
                for element in i:
                    yield element
            yield None

        for i, j in zip(_lazy_generator(word1), _lazy_generator(word2)):
            if i != j:
                return False
        return True

S = Solution()
# print(S.arrayStringsAreEqual(word1 = ["ab", "c"], word2 = ["a", "bc"]))
print(S.Lazely_arrayStringsAreEqual(["abcddefg"], ["abc", "d", "defg"]))