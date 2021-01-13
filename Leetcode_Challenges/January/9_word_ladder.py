from typing import List
from collections import defaultdict, deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # more efficient method for creating Adjacency list
        def _pre_processing_word_list(data: List) -> dict:
            word_len = len(beginWord)
            combo_dict = defaultdict(list)

            for item in data:
                for i in range(word_len):
                    # Key is the generic word
                    # Value is a list of words which have the same intermediate generic word.
                    combo_dict[item[:i] + "*" + item[i + 1:]].append(item)

            return combo_dict

        # building adjacency list
        def _build_adjacency_list(data: List) -> dict:
            adjacency_list = {}
            visited = {}
            for word in data:
                visited[word] = True
                adjacency_list[word] = []
                for child in wordList:
                    if child != word and not visited.get(child):
                        diff = sum([1 for i in child if i not in word])
                        if diff == 1:
                            adjacency_list[word].append(child)
            return adjacency_list

        all_combo_dict = _pre_processing_word_list(wordList)
        L = len(beginWord)
        queue = deque([(beginWord, 1)])
        visited = {beginWord: True}
        while queue:
            current_word, level = queue.popleft()
            for i in range(L):
                # Intermediate words for current word
                intermediate_word = current_word[:i] + "*" + current_word[i + 1:]

                # Next states are all the words which share the same intermediate state.
                for word in all_combo_dict[intermediate_word]:
                    # If at any point if we find what we are looking for
                    # i.e. the end word - we can return with the answer.
                    if word == endWord:
                        return level + 1
                    # Otherwise, add it to the BFS Queue. Also mark it visited
                    if word not in visited:
                        visited[word] = True
                        queue.append((word, level + 1))
                all_combo_dict[intermediate_word] = []
        return 0


    def brute_force(self, beginWord: str, endWord: str, wordList: List[str], count: int) -> int:
        if not wordList:
            return 0
        for word in wordList:
            diff = sum([1 for i in word if i not in beginWord])
            if word == endWord:
                return count
            if diff == 1:
                arr = wordList
                arr.remove(word)
                return self.brute_force(word, endWord, arr, count + 1)


S = Solution()
print(S.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
