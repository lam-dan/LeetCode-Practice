class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Pair cars by (position, speed) and sort by position descending
        # → ensures we process cars from closest to the target back toward the start.
        # Why? Because front cars "set the pace" for all cars behind them.
        cars = sorted(zip(position, speed), reverse=True)

        fleets = 0
        last_duration = 0.0   # travel time of the last fleet leader (the slowest car ahead)

        for pos, spd in cars:
            # Travel duration = how long this car would take to reach the target if it went alone.
            # Not a wall-clock "arrival time", but a relative duration (distance / speed).
            travel_duration = (target - pos) / spd

            # Key greedy logic:
            # - If this car's duration is GREATER than the fleet ahead,
            #   it is slower → cannot catch up → starts a NEW fleet.
            # - If this car's duration is LESS or EQUAL, it will eventually catch up
            #   (maybe right at the finish line) → merges into that fleet.
            if travel_duration > last_duration:
                fleets += 1
                last_duration = travel_duration  # update fleet pace to this slower car
            else:
                # merges with fleet ahead → do nothing
                pass

        return fleets


"""
Intuition:

This problem is really asking for the MAXIMUM number of fleets that can arrive
at the target. Since cars cannot pass each other, fleets can only MERGE, never split.
So every time we find a car that is "too slow to catch up" to the fleet ahead,
we have discovered a new distinct fleet.

Steps:
1. Sort cars by position (front → back).
2. Convert each car into its travel_duration = (target - pos) / speed.
3. Walk from front to back:
   - If a car is slower (duration > last_duration), start a new fleet.
   - If a car is faster (duration ≤ last_duration), it merges into the fleet ahead.
4. Count how many times we had to start a new fleet → that's the maximum possible fleets.

Example:
target = 12
cars = [(10,2), (8,1), (5,2)]
durations = [1.0, 4.0, 2.5]

- Car at 10 → 1h → new fleet (fleets=1, last_duration=1)
- Car at 8 → 4h → slower → new fleet (fleets=2, last_duration=4)
- Car at 5 → 2.5h ≤ 4h → merges into fleet with car at 8
Answer = 2 fleets
"""