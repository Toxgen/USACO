import sys

# try:
#     sys.stdin = open("in-n-out/input.in", "r")
#     sys.stdout = open("in-n-out/output.out", "w")
# except Exception as e:
input = sys.stdin.read
print = sys.stdout.write

a = input().split("\n")
index = 0

for x in range(1, int(a[0]) + 1):
    n = list(map(int, a[x].split(" ")))
    if n.count(1) >= 2:
        index += 1

print(str(index))