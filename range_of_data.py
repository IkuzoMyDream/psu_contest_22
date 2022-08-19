#1.) range of data
round = int(input())
l = []

while True:
    n = [int(i) for i in input().split()]
    for i in n:
        l.append(i)
    if len(l) == round:
        break
print(max(l) - min(l))
