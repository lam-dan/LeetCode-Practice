class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        
        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                prev_day_temp_index = stack.pop()
                result[prev_day_temp_index] = i - prev_day_temp_index
            stack.append(i)
        return result





        return answer
