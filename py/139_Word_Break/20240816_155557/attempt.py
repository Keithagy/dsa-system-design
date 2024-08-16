from typing import List, Optional


class Solution:
    class Trie:
        lowercase_letter_count = 26

        class Node:
            def __init__(self, val: str) -> None:
                self.val = val
                self.isTerminal = False
                self.next: List[Optional[Solution.Trie.Node]] = [
                    None for _ in range(Solution.Trie.lowercase_letter_count)
                ]

        def __init__(self) -> None:
            self.root: Solution.Trie.Node = Solution.Trie.Node("")

        def insert(self, s: str) -> None:
            cur = self.root
            for c in s:
                idx = ord(c) - ord("a")
                next_node = (
                    Solution.Trie.Node(c) if cur.next[idx] is None else cur.next[idx]
                )
                cur.next[idx] = next_node
                cur = next_node
            cur.isTerminal = True

        def dfs(self, s: str) -> bool:
            start_char = s[0]
            idx = ord(start_char) - ord("a")
            start_node = self.root.next[idx]
            if start_node is None:
                return False
            queue = [(start_node, 0)]  # dfs
            while queue:
                (node, string_i) = queue.pop()
                print(node.val, node.isTerminal, node.next, string_i)
                if string_i >= len(s) - 1:
                    # Gotten to end of the string
                    if node.isTerminal:
                        return True
                    else:
                        continue
                next_c = s[string_i + 1]
                next_c_idx = ord(next_c) - ord("a")
                next_node = node.next[next_c_idx]
                if next_node is None:
                    # Two possibilities: time to start a new word or failed to match
                    if node.isTerminal:
                        new_word = self.root.next[next_c_idx]
                        if new_word:
                            queue.append((new_word, string_i + 1))
                else:
                    # If able to continue down current branch of trie, should
                    # However, should also consider non-greedy possibility of starting a new word
                    possible_new_word_node = self.root.next[next_c_idx]
                    if possible_new_word_node:
                        queue.append((possible_new_word_node, string_i + 1))
                    queue.append((next_node, string_i + 1))
            return False

    # Example:
    # catsandog
    # ["cats","og","and","cat"]
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie = Solution.Trie()
        for word in wordDict:
            trie.insert(word)
        return trie.dfs(s)

