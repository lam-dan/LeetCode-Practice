class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        access_history = defaultdict(list)

        for name, time in zip(keyName, keyTime):
            clock = time.split(":")
            hours, minutes = int(clock[0]), int(clock[1])
            total_minutes = hours * 60 + minutes
            access_history[name].append(total_minutes)

        result = []

        print(access_history)

        for name, time in access_history.items():
            time.sort()
            left = 0
            for i in range(len(time)):
                while time[i] - time[left] > 60:
                    left += 1
                access_count = i - left + 1
                if access_count >= 3:
                    result.append(name)
                    break
        return sorted(result)
                