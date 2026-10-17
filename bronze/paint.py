import sys

try: 
    sys.stdin = open("paint.in", "r")
    sys.stdout = open("paint.out", "w")
except Exception as e:
    input = sys.stdin.readline
    print = sys.stdout.write

count = 0

n = sys.stdin.read().split("\n")

# print(f"{str(n)}")
for x in [0, 1]:
    n[x] = list(map(int, n[x].split(" ")))

n = n[0] + n[1]
fences = [False for x in range(0, 100)]

for x in range(n[0], n[1]):
    fences[x] = True

for x in range(n[2], n[3]):
    fences[x] = True

for x in fences:
    if x:
        count += 1

print(count)

