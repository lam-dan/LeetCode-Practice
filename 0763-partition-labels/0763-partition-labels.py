class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}

        for i in range(len(s)-1, -1, -1):
            char = s[i]
            if char in lastIndex:
                continue
            else:
                lastIndex[char] = i
        
        # Things to keep track of:
        length = 0 # length of current substring
        end = 0 # ending index - allows to identify the end of a substring and store the results
        res = [] # result array that we return containing lengths of all substrings

        for i in range(len(s)):
            char = s[i]
            length += 1
            # As we iterate through the characters and get their last indexes
            # we want to confirm what the new maximum ending index for the substring is
            end = max(end, lastIndex[char])
            # logic for knowing when we've reached the end of a substring
            if i == end:
                res.append(length)
                length = 0
        return res







        