from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        print(dic)
        for word in strs:
            # [0 0 0 0 0 0 0 0....]
            char_counter = [0] * 26
            for char in word:
                char_counter[ord('a') - ord(char)] += 1
            dic[tuple(char_counter)].append(word)
        print(dic)
        return list(dic.values())

        
