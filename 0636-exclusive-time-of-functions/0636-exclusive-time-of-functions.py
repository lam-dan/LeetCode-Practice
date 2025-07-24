class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = []                # Stack to track currently running function IDs
        res = [0] * n             # Result list to store exclusive time for each function
        prev_time = 0             # Tracks the previous timestamp we've processed

        # Iterate through each log entry
        for i in range(len(logs)):
            # Split log into function ID, type ('start' or 'end'), and timestamp
            fn_id, typ, time_stamp = logs[i].split(":")
            fn_id = int(fn_id)             # Convert function ID to integer
            current_time = int(time_stamp)  # Convert timestamp to integer

            if typ == "start":
                if stack:
                    # A function is already running; add time since prev_time
                    # to the function at the top of the stack
                    res[stack[-1]] += current_time - prev_time

                # Push the new function onto the stack (it is now running)
                stack.append(fn_id)
                # Update prev_time to this function's start time
                prev_time = current_time

            else:  # typ == "end"
                # Function ends; pop it from the stack
                # Its runtime is (current_time - prev_time + 1), inclusive
                res[stack.pop()] += current_time - prev_time + 1
                # Update prev_time to the time when the next function will resume
                prev_time = current_time + 1

        # After processing all logs, return the exclusive time for each function
        return res




            