class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = []                # Stack to store the IDs of currently running functions
        res = [0] * n             # Result array to store exclusive time for each function
        prev_time = 0             # Tracks the time of the last event

        for i in range(len(logs)):
            fn_id, typ, timestamp = logs[i].split(":")   # Parse the log entry
            fn_id = int(fn_id)                           # Convert function ID to int
            current_time = int(timestamp)                # Convert timestamp to int

            if typ == "start":
                if stack:
                    # Add elapsed time to the function on top of the stack
                    res[stack[-1]] += current_time - prev_time
                stack.append(fn_id)                      # Start new function
                prev_time = current_time                 # Update prev_time
            else:
                # End current function and include the current_time (inclusive)
                res[stack.pop()] += current_time - prev_time + 1
                prev_time = current_time + 1             # Resume next function after this

        return res                                        # Return the exclusive time per function




            