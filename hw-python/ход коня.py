a_y = int(input())
a_x = int(input())
b_y = int(input())
b_x = int(input())
if (b_x-a_x == 1 and (b_y - a_y == 2 or b_y - a_y == -2)) or (b_x - a_x == 2 and (b_y - a_y == 1 or b_y - a_y == -1)) or (b_x - a_x == -1 and (b_y-a_y == 2 or b_y - a_y == -2)) or (b_x - a_x ==-2 and (b_y - a_y == 1 or b_y - a_y == -1)):
                                                                                                                                                                                     
    print('YES')
else:
    print('NO')
