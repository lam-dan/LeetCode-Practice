class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)  # sort by position descending
        fleets = 0
        last_time = 0   # arrival time of the last fleet leader

        for pos, spd in cars:
            time_to_target = (target - pos) / spd
            if time_to_target > last_time:     # new fleet forms
                fleets += 1
                last_time = time_to_target     # update last fleet's arrival time
            # else: merges into the last fleet → do nothing
        return fleets