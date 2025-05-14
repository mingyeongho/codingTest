# Time: 488ms
# Memory: 49152KB

import sys
input = sys.stdin.readline

def binarySearch(datas, target, startIndex, endIndex):
    if startIndex > endIndex:
        return None
    middle = (startIndex + endIndex) // 2

    if target == datas[middle]:
        return middle
    elif target < datas[middle]:
        return binarySearch(datas, target, startIndex, middle - 1)
    else:
        return binarySearch(datas, target, middle + 1, endIndex)

n = int(input().rstrip())
datas = list(map(int, input().split()))
datas.sort()
m = int(input().rstrip())
targets = list(map(int, input().split()))

for target in targets:
    result = binarySearch(datas, target, 0, n - 1)
    if result == None:
        print(0)
    else:
        print(1)

# 5
# 4 1 5 2 3
# 5
# 1 3 7 9 5