import sys

sys.stdin = open("promote.in", "r")
sys.stdout = open("promote.out", "w")

a = sys.stdin.read().split("\n")

B = list(map(int, a[0].split(" ")))
S = list(map(int, a[1].split(" ")))
G = list(map(int, a[2].split(" ")))
P = list(map(int, a[3].split(" ")))

deltaP = P[1] - P[0]

# promotion to platinum only came from gold 
promoteP = deltaP

# promotion from silver to gold
promoteG = P[1] + G[1] - (P[0] + G[0])

# promotion from bronze to silver
promoteS = P[1] + G[1] + S[1] - (P[0] + G[0] + S[0])

print(f"{promoteS}\n{promoteG}\n{promoteP}", end="")
