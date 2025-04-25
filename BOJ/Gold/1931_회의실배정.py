import sys
input = sys.stdin.readline

n = int(input())

meetings = [list(map(int, input().split())) for _ in range(n)]

# 회의 종료 시간이 일찍 끝나는 순서대로 정렬
meetings.sort(key=lambda x: (x[1], x[0]))

# 다음 회의가 이전 회의의 종료시간보다 뒤면 바로 시작
count = 1
endTime = meetings[0][1]
for i in range(1,n):
    if meetings[i][0] >= endTime:
        count += 1
        endTime = meetings[i][1]

print(count)

# 11
# 1 4
# 3 5
# 0 6
# 5 7
# 3 8
# 5 9
# 6 10
# 8 11
# 8 12
# 2 13
# 12 14
# result: 4