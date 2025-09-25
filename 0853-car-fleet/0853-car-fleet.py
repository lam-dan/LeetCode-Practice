class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Sort cars by position descending (closest to target first).
        # That way, each car only needs to consider the fleet directly in front.
        cars = sorted(zip(position, speed), reverse=True)

        fleets = 0
        last_time = 0   # arrival time of the last fleet leader (the slowest one so far)

        for pos, spd in cars:
            # How long this car would take to reach the target if it were alone
            time_to_target = (target - pos) / spd

            # Case 1: This car takes longer than the fleet ahead.
            # It cannot catch up before reaching the target → it forms a new fleet.
            if time_to_target > last_time:
                fleets += 1
                last_time = time_to_target   # update the "slowest fleet" arrival time to this one

            # Case 2: This car's time is <= last_time.
            # That means it would arrive sooner or at the same time if alone,
            # but since the road is one-lane, it must slow down and merge
            # with the fleet in front. So we do nothing here.

        return fleets