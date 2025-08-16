class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        access_history = defaultdict(list)

        for name, time in zip(keyName, keyTime):
            clock = time.split(":")
            hours = int(clock[0]) 
            minutes = int(clock[1]) 
            total = minutes + hours * 60
            access_history[name].append(total)

        print(access_history)

        result = []

        for name, time in access_history.items():
            print(time)
            time.sort()
            left = 0

            for right in range(len(time)):
                while time[right] - time[left] > 60:
                    left += 1
                if right - left + 1 == 3:
                    result.append(name)
                    break
        return sorted(result)

                


                
                



            
