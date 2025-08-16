class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Explanation: I wish the question was explained in bit more detail.
        # The question should be reframed as; Is there a combination of words in wordDict that can be used to recreate the original string s. Notice that I mentioned the word combination, this does not mean that you will need all the words in wordDict to recreate s (Using some words from wordDict as long as they perfectly recreate the string s; is a valid solution or word break). Also note that you can use the words in wordDict more than once.

        # Take this example for reference:
        # Input: "bb", ["a","b","bbb","bbbb"]
        # Expected: true

        # Here, word "b" from wordDict can be used to perfectly to recreate the string s = "b" + "b" , which is why the expected output is True. Note that we did not use all the words in the dictionary and still found a valid word break.

        # Now, let's take another example:
        # Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
        # Output: false

        # Here, no combination of words exist in wordDict that can perfectly recreate the input string s.
        # "cats" + "dog" will require "an" in wordDict in order to recreate s
        # "cats" + "and" will require "og" in wordDict in order to recreate s
        # "cat" + "sand" will require "og" in wordDict in order to recreate s
        # ... and so on.

        # The intuition is that you will have consider every combination of words in the wordDict, moreover these words can be used more than once when computing the combinations.
                # Explicit cache (memoization dictionary)
        # Key: index i (the end position in string s we are trying to segment)
        # Value: True/False = can s[:i+1] be segmented using words in wordDict?
        memo = {}

        def dfs(i):
            """
            Recursive helper function:
            dp(i) returns True if substring s[0..i] (inclusive) can be segmented
            into words from wordDict, otherwise False.
            """

            # Base case: if we've moved before the start of the string,
            # it means we've successfully segmented the entire string.
            if i < 0:
                return True

            # If we've already computed dp(i), return it directly.
            if i in memo:
                return memo[i]

            # Try every word in the dictionary
            for word in wordDict:
                L = len(word)  # length of current word

                # Check if the substring ending at index i matches this word.
                # The slice is s[i-L+1 : i+1] (inclusive of i).
                if i - L + 1 >= 0 and s[i - L + 1 : i + 1] == word:
                    # If it matches, recursively check the prefix before this word.
                    if dfs(i - L):
                        memo[i] = True   # store result in memo
                        return True      # found a valid segmentation

            # If no word works, store and return False
            memo[i] = False
            return False

        # Start the recursion from the last index of s (len(s)-1).
        # This asks: can the entire string be segmented?
        return dfs(len(s) - 1)
