class Solution:
    def maximumSwap(self, num: int) -> int:
        # Greedy with a suffix maximum, scanning right -> left.
        #
        # max_num:  largest digit seen so far to the RIGHT (the current suffix max)
        # max_idx:  index of that suffix-max digit (we prefer the rightmost occurrence)
        # swap_i:   index of the left position we want to improve (candidate to swap)
        # swap_j:   index of the best right-side digit to bring forward

        # Steps:
        # 1) Scan from right to left, maintaining (max_num, max_idx).
        # 2) If nums[i] < max_num, record (swap_i=i, swap_j=max_idx) — a better digit exists to the right.
        #    We keep updating swap_i as we move left so the final pair improves the leftmost possible position.
        # 3) After the scan, swap once using (swap_i, swap_j) and return the number.

        nums = list(str(num))  # Work with a list of characters so we can swap in-place.
        max_num = '0'
        max_idx = swap_i = swap_j = -1

        for i in range(len(nums) - 1, -1, -1):
            # Update suffix maximum if current digit is strictly larger.
            # (Strict '>' keeps the rightmost occurrence of equal digits.)
            if nums[i] > max_num:
                max_num, max_idx = nums[i], i
            # If current digit is smaller than the best to its right,
            # record a swap opportunity (move a bigger digit left).
            if nums[i] < max_num:
                swap_i, swap_j = i, max_idx

        # Perform the single allowed swap (if no opportunity was found, this is effectively a no-op).
        temp = nums[swap_i]
        nums[swap_i] = nums[swap_j]
        nums[swap_j] = temp

        # Alternative Pythonic swap:
        # nums[swap_i], nums[swap_j] = nums[swap_j], nums[swap_i]

        return int("".join(nums))
