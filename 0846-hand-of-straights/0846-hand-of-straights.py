class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)

        if n % groupSize != 0:
            return False

        counter = Counter(hand)
        sorted_counter_list = sorted(counter) # Converts freq map into a list sorted by key
        # print(sorted(cnt, key=lambda x: cnt[x])) - if you want to sorted it by value

        for i in range(len(sorted_counter_list)): # Sort unique values from counter
            num = sorted_counter_list[i]
            if num not in counter:            # already consumed by earlier steps
                continue

            count = counter[num]
            
            
            for k in range(num, num + groupSize): # Example: Loop 1 -> 1 + 3 = 4, so loop 1,2,3
                if k not in counter:
                    return False
                if counter[k] < count:
                    return False
                counter[k] -= 1
                if counter[k] == 0:
                    del counter[k]
        return True
                

                




