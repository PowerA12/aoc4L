with open('day1', 'r') as f:
    left = []
    right = []
    s = 0
    output = f.read().split('\n')[0:-1]
    for i in output:
        val = i.split('   ')
        left.append(int(val[0]))
        right.append(int(val[1]))
    left = sorted(left)
    right = sorted(right)
    for j in range(len(left)):
        s += abs(left[j] - right[j])
    print(s)
