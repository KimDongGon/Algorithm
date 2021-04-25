import sys

N = int(sys.stdin.readline())
files = list(map(int, sys.stdin.readline().split()))
disk = int(sys.stdin.readline())

count = 0

for file in files:
    if file != 0:
        if file <= disk:
            count += 1
        else:
            count += file // disk + (1 if file % disk != 0 else 0)

answer = disk * count
print(answer)