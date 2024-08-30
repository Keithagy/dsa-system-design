from collections import defaultdict
from typing import Counter, List
import heapq


class Solution:
    # initialize a counter for words
    # iterate through words to get max heap leaderboard
    # return reversed list
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
      word_count_rev = Counter(words)
      word_counts = defaultdict(list)
      for word in word_count_rev:
        word_count = word_count_rev[word]
        word_counts[word_count].append(word)
      
      len_rank = sorted(word_counts.keys(), reverse=True)
      cur_rank = 0
      result=[]
      while k > 0:
        words_in_cur_rank = sorted(word_counts[len_rank[cur_rank]])
        if len(words_in_cur_rank) <= k:
          result.extend(words_in_cur_rank)
          k -= len(words_in_cur_rank)
          cur_rank+=1
        else:
          result.extend(words_in_cur_rank[:k])
          k -= len(words_in_cur_rank[:k])
      return result

      # word_counts = Counter(words)
      # minheap = []
      # for word in word_counts:
      #   count = word_counts[word]
      #   if len(minheap) < k:
      #     heapq.heappush(minheap, (count, word))
      #   else:
      #     if minheap[0][0] < count:
      #       heapq.heapreplace(minheap, (count,word))
      #     elif minheap[0][0] == count:
      #       if minheap[0][1] >= count:
      #         heapq.heapreplace(minheap, (count,word))
      # print(minheap)
      # return [entry[1] for entry in minheap[::-1]]
