import sys

# sys.stdin = open("in-n-out/input.in", "r")
# sys.stdout = open("in-n-out/output.out", "w")

sys.stdin = open("buckets.in", "r")
sys.stdout = open("buckets.out", "w")

a = sys.stdin.read().split("\n")
a.pop(-1)

B = [(j.find("B") + 1, i + 1) for i, j in enumerate(a) if j.find("B") != -1][0]
R = [(j.find("R") + 1, i + 1) for i, j in enumerate(a) if j.find("R") != -1][0]
L = [(j.find("L") + 1, i + 1) for i, j in enumerate(a) if j.find("L") != -1][0]

answer = abs(B[0] - L[0]) + abs(B[1] - L[1])
betweenXaxis = list(range(min(B[0], L[0]) + 1, max(B[0], L[0])))
betweenYaxis = list(range(min(B[1], L[1]), max(B[1], L[1])))
# ```print(R)
# print(betweenXaxis, betweenYaxis)
# print(B[0], B[1], L[0], L[1])```
if (B[0] == L[0] and R[1] in betweenYaxis and R[0] == B[0]) or (B[1] == L[1] and R[0] in betweenXaxis and R[1] == B[1]):
    answer += 2
print(answer - 1)