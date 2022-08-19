#2.) reverse digits
number = input()
l = [number[::-1]]
while True:
    number = input()
    if number == '0':
        break
    l.append(number[::-1])
print(*l, sep='\n')
