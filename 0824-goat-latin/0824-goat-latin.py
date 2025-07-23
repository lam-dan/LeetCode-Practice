class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        words = sentence.split(" ")
        vowels = {
            'a', 'e', 'i', 'o', 'u'
        }
        result = []
        
        for i in range(len(words)):
            new_word = ""
            if words[i][0].lower() in vowels:
                new_word = words[i] + "ma"
            else:
                new_word = words[i][1:] + words[i][0] + "ma"
            new_word += (i + 1) * "a"
            result.append(new_word)
        return " ".join(result)

        # Time Complexity: O(n²)
        #   - n = number of words in the sentence
        #   - For each word:
        #       • We may perform slicing (word[1:] and word[0]) → O(m), where m is the word length
        #       • We concatenate strings like "ma" and "a" * (i + 1)
        #         The "a" suffix grows linearly: 1 + 2 + 3 + ... + n = O(n²)
        #   - So overall: O(n * m + n²) = O(n²) in the worst case when m is small and "a" tails dominate
        #   - Final " ".join(...) takes O(total characters), which is also O(n²)

        # Space Complexity: O(n²)
        #   - Each word grows due to "ma" and the trailing "a"s.
        #   - Storing n transformed words results in total output size of O(n²)

        





