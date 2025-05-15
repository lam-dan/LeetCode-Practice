from collections import Counter
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        total_length = 0

        for word in words:
            number_of_deletes = 0
            charsCounter = Counter(chars)
            charWordCounter = list(word)
            print(charsCounter)
            print(charWordCounter)
            for char in charWordCounter:
                if char not in charsCounter:
                    break
                else:
                    print("char", char)
                    print("char count", charsCounter[char])
                    charsCounter[char] -= 1
                    print("char count", charsCounter[char])
                    if charsCounter[char] == 0:
                        print("deleting char", char)
                        del charsCounter[char]
                    number_of_deletes += 1
                    print("number_of_deletes", number_of_deletes)
            # print("word", word)
            # print("number_of_deletes", number_of_deletes)
            if number_of_deletes == len(word):
                total_length += number_of_deletes
        print(total_length)
        return total_length



