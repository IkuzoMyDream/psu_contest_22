# #4.) max distance

position = [int(i) for i in input().split()]
list_xyz = [[int(i) for i in position]]

while True:
    position = [int(i) for i in input().split()]
    if position[0] == 0 and position[1] == 0 and position[2] == 0:
        break
    list_xyz.append(position)

#[[9, 10, 5], [8, 10, 5], [7, 9, 3], [7, 10, 5]]
list_distance = []
for index,item in enumerate(list_xyz):
    for i,j in enumerate(list_xyz):
        if j == item:
            continue
        d = ( ((item[0] - j[0] ) ** (2)) + ((item[1] - j[1] ) ** (2)) + ((item[2] - j[2] ) ** (2)) ) **(1/2)
        list_distance.append(d)
print(f'{max(list_distance):.2f}')
