class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        counter = Counter(hand)
        hand.sort()

        for i in range(len(hand)):
            num = hand[i]
            if counter[num]:
                for j in range(num, num + groupSize):
                    counter[j] -= 1
                    if counter[j] < 0:
                        return False
        return True