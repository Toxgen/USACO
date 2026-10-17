import sys

try:
    sys.stdin = open("in-n-out/input.in", "r")
    sys.stdout = open("in-n-out/output.out", "w")
except Exception as e:
    input = sys.stdin.read
    print = sys.stdout.write

a = list(map(int, input().split(" ")))

k = a[0]
n = a[1]
w = a[2]

t: int = 0
for d in range(1, w + 1):
    t += k * d

print(str(max(t - n, 0)))