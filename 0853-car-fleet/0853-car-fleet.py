class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Pair cars as (position, speed) and sort by position descending
        # → ensures we process cars from closest to the target back
        cars = sorted(zip(position, speed), reverse=True)

        fleets = 0
        last_duration = 0.0   # travel time of the fleet ahead (the slowest leader)

        for pos, spd in cars:
            # How long this car would take to reach the target if it went alone
            travel_duration = (target - pos) / spd

            if travel_duration > last_duration:
                # This car is slower than the fleet ahead → cannot catch up
                # → starts a new fleet
                fleets += 1
                last_duration = travel_duration  # new fleet sets the "pace"

        return fleets