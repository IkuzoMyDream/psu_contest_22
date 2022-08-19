#3.) count numeric characters

pharse = input()
ans = [i for i in pharse if i.isdigit()]

while True:
    pharse = input()
    if pharse == 'END':
        break
    for i in pharse:
        if i.isdigit():
            ans.append(i)
print(len(ans))
