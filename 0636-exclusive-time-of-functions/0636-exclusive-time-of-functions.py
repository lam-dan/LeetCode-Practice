class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = [] # Stack to store the IDs of functions currently running
        res = [0] * n # Result array to store exclusive time at function i
        prev = 0

        for i in range(len(logs)):
            fn_id, typ, timestamp = logs[i].split(":") # Parse the log
            fn_id = int(fn_id) # Convert function ID to int
            current_time = int(timestamp) # Convert timetsamp to int

            if typ == "start":
                if stack:
                    # Add time since last update to the function currently running
                    res[stack[-1]] += current_time - prev_time
                stack.append(fn_id)
                prev_time = current_time
            else:
                 # Current function ends now; include this timestamp (+1)
                 res[stack.pop()] += current_time - prev_time + 1
                 prev_time = current_time + 1
        return res




            