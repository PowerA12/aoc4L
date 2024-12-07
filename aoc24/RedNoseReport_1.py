with open('day2', 'r') as f:
    safe = 0 
    for i in f.readlines():
        diffs = []
        i = list(map(int, i.replace('\n', '').split(" ")))
        if sorted(i) == i or sorted(i)[::-1] == i:
            for j in range(len(i) - 1):
                diff = abs(i[j] - i[j+1])
                diffs.append(diff)
            if max(diffs) <= 3 and min(diffs) >= 1:
                safe += 1
    print(safe)
