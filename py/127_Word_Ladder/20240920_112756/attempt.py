from typing import List
from collections import defaultdict, deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        If you build a trie of all words in the word list,
        then for each character you could see which other words you can hop onto
        then you just apply a backtracking algorithm

        but the key question would be how you can track the number of switches

        I need to answer the question, for a given word, which words can i hop onto?
        [hot, dot, dog, lot, log, cog]
        from "hit":
        change h >> nothing
        change i >> hot
        change t >> nothing

        from "hot":
        change h >> dot, lot
        change o >> nothing
        change t >> nothing

        and so on.
        My trie probably needs to contain a mapping of which words have this letter,
        maybe not a trie. you just need to build the graph of possible state transitions, then traverse it bfs and see if you can get to end word.
        this seems like a pretty inefficient algorithm though. it's n^2 to build the graph from wordList >> not too sure atm how to optimize this
        """

        wordSet = set(wordList)

        q = deque([(beginWord, 1)])
        visited = set([beginWord])
        while q:
            (word, pathLength) = q.popleft()
            if word == endWord:
                return pathLength
            for i in range(len(word)):
                for c in [chr(ord) for ord in range(ord("a"), ord("z") + 1)]:
                    candidate = word[:i] + c + word[i + 1 :]
                    if candidate in wordSet and candidate not in visited:
                        visited.add(candidate)
                        q.append((candidate, pathLength + 1))
        return 0

