class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1

        needle_count = 0
        index = None

        for i in range(len(haystack)):
            j = 0
            while i < len(haystack) and haystack[i] == needle[j]:
                if j == 0:
                    index = i
                needle_count += 1
                i += 1
                j += 1
                if needle_count == len(needle):
                    return index
            needle_count = 0
        return -1




                
            

