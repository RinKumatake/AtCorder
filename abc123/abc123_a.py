# https://atcoder.jp/contests/abc123/tasks/abc123_a

antennas =[]
for i in range(5):
    antenna = int(input())
    antennas.append(antenna)
k = int(input())
antennas_max = max(antennas)
antennas_min = min(antennas)
antennas_distance_max = antennas_max - antennas_min
if k < antennas_distance_max:
    print(":(")
else:
    print("Yay!")