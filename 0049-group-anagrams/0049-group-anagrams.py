class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # Dictionary grouping key based on anagram values
        # {[0101010101010101)]: ['n','a','t'],['t','a','n'] }

        anagram_dic = defaultdict(list)
        for word in strs:
            char_counter = [0] * 26
            for char in word:
                key = ord(char) - ord('a')
                char_counter[key] += 1
            anagram_dic[tuple(char_counter)].append(word)
        return list(anagram_dic.values())

