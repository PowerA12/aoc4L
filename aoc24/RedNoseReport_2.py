def isSafe(safe):
    diffs = []
    if sorted(safe) == safe or sorted(safe)[::-1] == safe:
        for num in range(len(safe) - 1):
            diff = abs(safe[num] - safe[num+1])
            diffs.append(diff)
        if max(diffs) <= 3 and min(diffs) >= 1:
            return True
    return False
with open('day2', 'r') as f:
    lines = [list(map(int, x.replace('\n', '').split(' '))) for x in f.readlines()]
    totalSafe = 0
    for line in range(len(lines)):
        if isSafe(lines[line]):
            totalSafe += 1
        elif isSafe(lines[line]) == False:
            for i in range(len(lines[line])):
                test = lines[line].copy()
                test.pop(i) # .remove() removed out of order, so use index 
                if isSafe(test):
                    totalSafe += 1
                    break
    print(totalSafe)

