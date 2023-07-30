n = int(input())
l = [int(i) for i in input().split()]

k = max(l)
h = float('-inf')

for i in l:
    if k > i > h:
        h = i

print(h)
