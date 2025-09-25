class Solution(object):
    def minStartValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = 0      # current_sum: running prefix sum (like current altitude on the hike)
        min_sum = 0    # min_prefix_sum: lowest altitude (valley) seen so far

        # Traverse nums and compute the prefix sums
        for i in range(len(nums)):
            total += nums[i]                 # update current altitude
            min_sum = min(min_sum, total)    # record the lowest altitude reached

        # Mental model (line graph):
        # --------------------------------------
        # If we start at 0 and plot the prefix sums as a line graph,
        # each step moves us up (positive num) or down (negative num).
        #
        # Example: nums = [-3, 2, -3, 4, 2]
        # Prefix sums = [-3, -1, -4, 0, 2]
        #
        # Graphing these gives a wavy line that dips as low as -4.
        #
        # The rule says: the line (step-by-step total) must never go below 1.
        # So, we must "lift" the entire line upward until its lowest point
        # (the valley at -4) is exactly at 1.
        #
        # That means:
        #   startValue = 1 - min_sum
        #
        # In this example: min_sum = -4 → startValue = 5.
        #
        # On the graph, it looks like shifting the whole line upward by +5,
        # so the lowest point now sits right on y = 1 and everything else is ≥ 1.
        # --------------------------------------

        return 1 - min_sum
            
            

            

            




