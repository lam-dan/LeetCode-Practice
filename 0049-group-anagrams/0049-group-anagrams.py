from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        store = defaultdict(list)
        for word in strs:
            counter = [0] * 26
            for char in word:
                counter[ord('a')- ord(char)] += 1
            store[tuple(counter)].append(word)
        return list(store.values())


