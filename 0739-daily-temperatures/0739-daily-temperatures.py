class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # 2 pointers solution
        # iterate backwards since we don't worry about going out of bounds
        # jumping indexes 
        result = [0] * len(temperatures)
        # hottest = 0
        hottest = temperatures[len(temperatures)- 1]

        for i in range(len(temperatures) - 2, -1, -1):
            if temperatures[i] >= hottest:
                hottest = temperatures[i]
                continue

            j = i + 1

            while temperatures[j] <= temperatures[i]:
                j += result[j]

            result[i] = j - i

        return result