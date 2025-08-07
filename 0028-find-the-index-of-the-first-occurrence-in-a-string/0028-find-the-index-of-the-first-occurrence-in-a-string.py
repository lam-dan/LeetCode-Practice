class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Knutt Morris KMP Algorithm for O(n) time complexity where n is the number of 
        # elements in haystack
        # However, the trade off is O(m) space where m is the longer array of haystack or needle   

        lps = self.build_lps(needle)
        print("lps", lps)
        i = 0
        j = 0

        while i < len(haystack):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
                if j == len(needle):
                    return i - j
            else:
                if j > 0:
                    j = lps[j - 1]
                else:
                    i += 1
        return -1

    def build_lps(self, needle):
        lps = [0] * len(needle)
        length = 0

        i = 1
        while i < len(needle):
            if needle[i] == needle[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length > 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps
