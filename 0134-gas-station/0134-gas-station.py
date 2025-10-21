class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # total_gain keeps track of whether the total gas available across all stations
        # is enough to cover the total travel cost.
        # If total_gain < 0 at the end, it's impossible to complete the circuit.
        total_gain = 0

        # curr_gain keeps track of the current fuel balance as we move from station to station.
        # If curr_gain ever drops below 0, it means we cannot reach the next station
        # from the current starting point.
        curr_gain = 0

        # answer will store the index of the station that can serve as the valid start.
        answer = 0

        # Loop through each gas station
        for i in range(len(gas)):
            # The net gain or loss at this station
            gain = gas[i] - cost[i]

            # Update both total and current gain
            total_gain += gain
            curr_gain += gain

            # If at any point curr_gain drops below 0, we cannot reach the next station
            # from our current start. That means the current segment is invalid.
            # So, reset curr_gain to 0 and set the next station as the new potential start.
            if curr_gain < 0:
                curr_gain = 0
                answer = i + 1  # move start index to next station

        # After completing the loop:
        # - If total_gain >= 0, a valid start exists (guaranteed unique).
        # - Otherwise, no valid start can complete the circuit.
        return answer if total_gain >= 0 else -1