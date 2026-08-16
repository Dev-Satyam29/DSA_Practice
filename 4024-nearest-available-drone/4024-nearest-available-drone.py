class Solution:
    def nearestDrone(self, drones: list[list[int]], target: list[int]) -> int:
        freq = {}
        for i in range(len(drones)):
            man = abs(drones[i][0] - target[0]) + abs(drones[i][1] - target[1])
            if man <= drones[i][2]:
                freq[i] = man
        sorted_dict = dict(sorted(freq.items(), key=lambda x: x[1]))
        if len(sorted_dict) == 0:
            return -1
        else:
            return next(iter(sorted_dict))