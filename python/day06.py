def number_wins(time, distance):
    total = 0
    for i in range(1, time):
        d = i*(time-i)
        total += d>distance
    return total

with open('../input/input_6.txt', 'r') as file:
    for line in file:
        words = line.split()
        if words[0] == 'Time:':
            time = [int(num) for num in words[1:]]
        elif words[0] == 'Distance:':
            distance = [int(num) for num in words[1:]]

total = 1
for t, d in zip(time, distance):
    total *= number_wins(t, d)
print("first part answer: ", total)

t = number_wins(58819676, 434104122191218)
print(f"second part answer: {t}")