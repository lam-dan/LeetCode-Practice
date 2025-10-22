class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # Total number of cards
        N = len(hand)

        # If total cards can't be divided evenly into groups, it's impossible
        if N % groupSize != 0:
            return False

        # Count how many of each card value we have
        freq = Counter(hand)

        # Sort cards so we always start from the smallest number
        hand.sort()

        # Iterate through every card using index-based loop
        for i in range(N):
            num = hand[i]  # current card value

            # If this card still exists in our counter, try to start a group
            if freq[num] > 0:
                # Attempt to form a consecutive sequence starting at 'num'
                for cur in range(num, num + groupSize):
                    freq[cur] -= 1  # use one copy of this card
                    # If count goes below zero, this card wasn't available
                    if freq[cur] < 0:
                        return False

        # If all groups are successfully formed, it's a valid hand
        return True