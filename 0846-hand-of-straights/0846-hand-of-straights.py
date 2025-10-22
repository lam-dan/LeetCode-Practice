class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        counter = Counter(hand)
        hand.sort()
        # total = []
        for i in range(len(hand)):
            num = hand[i]
            if counter[num] != 0:
                # result = []
                for j in range(num, num + groupSize):
                    counter[j] -= 1
                    # result.append(j)
                    if counter[j] < 0:
                        return False
                # total.append(result)
        # print(total)
        return True

        # Time Complexity is O(n*logn + n * k) n is the number of numbers in the hand, and k is the groupSize
        # of each hand since we have a nested for loop.
        # Space Complexity is O(n) since we create hash map to count the frequency