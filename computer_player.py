from asyncio.windows_events import INFINITE
import pygame
from positions import *
from draw import *
import queue

def analyze(my_board, next_player, x, y, rank):  # phân tích bàn cờ nếu như thêm vào vị trí (x, y)
    board = coppyList(my_board)
    board[x][y] = next_player
    if have_five(board, next_player, x, y):
        return 1e18
    board[x][y] = -next_player
    if have_five(board, -next_player, x, y):
        return 1e18
    board[x][y] = next_player
    pointAttack = process(board, next_player, x, y, rank)
    # pointAttack = max(pointAttack, four_in_a_row(board, next_player, x, y, '1'))
    # pointAttack = max(pointAttack, three_in_a_row(board, next_player, x, y, '1'))
    # pointAttack = max(pointAttack, two_in_a_row(board, next_player, x, y, '1'))
    board[x][y] = -next_player
    pointDefense = process(board, -next_player, x, y, rank)
    # pointDefense = max(pointDefense, four_in_a_row(board, next_player * -1,x , y, '2'))
    # pointDefense = max(pointDefense, three_in_a_row(board, next_player * -1, x, y, '2'))
    # pointDefense = max(pointDefense, two_in_a_row(board, next_player * -1,x, y, '2'))
    board[x][y] = 0
    return max(pointDefense, pointAttack)

def analyze_current_move(table, next_player):  # phần tôi làm
    point, position_x, position_y = 0, 0, 0
    ntable = len(table)
    for x in range(ntable):
        for y in range(ntable):
            if table[x][y] == 0:
                cur_point = analyze(table, next_player, x, y, 1)
                if point < cur_point:
                    point = cur_point
                    position_x = x
                    position_y = y
    return (point, position_x, position_y)

def deep_analyze(board):  # phần mọi người làm, đưa trang thái bàn cờ vào queue, lấy từng cái ra 1 rồi phân tích và chọn nước tối ưu
    q = queue.Queue()
    table = coppyList(board)
    q.put((table, 0, -1, 0, 0, 0)) # table, dept, next_player, x, y, result
    answer = (-1e18, 0, 0) # point, x, y
    while q.qsize() > 0 :
        container = q.get()
        list = coppyList(container[0])
        dept = container[1]
        nxt = container[2]
        x , y = container[3], container[4]
        result = container[5]
        # print("dept = ", dept, ' ', x, ' ', y, ' ', result)
        # if dept >= 2 :print(dept)
        if dept >= 2:
            # print(result)
            if result > answer[0]:
                # print(x, ' ', y)
                answer = (result, x, y)
            continue
        nlist = len(list)
        if dept % 2 == 1 :
            new_l = coppyList(list)
            answer = (0, 0, 0)
            answer = enemy_max_points(new_l, 1, 2)
            new_l[answer[1]][answer[2]] = 1
            q.put((new_l, dept + 1, -1, x, y, result - answer[0]))
            continue
        for i in range(nlist):
            for j in range(nlist):
                if list[i][j] == 0:
                    new_list = coppyList(list)
                    new_result = result
                    if dept % 2 == 0:
                        if dept == 0 :
                            point = analyze(list, nxt, i, j, 1)
                        else :
                            point = analyze(list, nxt, i, j, 3)
                        new_result += point
                        new_list[i][j] = -1                        
                    else:
                        point = analyze(list, nxt, i, j, 2)
                        new_result -= point
                        new_list[i][j] = 1
                    if dept == 0:
                        q.put((new_list, dept + 1, -nxt, i, j, new_result)) # đưa điểm mới và nước đi đầu tiên chọn trong chuỗi nước đi
                    else :
                        q.put((new_list, dept + 1, -nxt, x, y, new_result)) # cập nhật điểm mới cho nước đi x, y

    return answer

# screen: màn hình hiện đang chơi, board: mảng 2 chiều thể hiện trạng thái của bàn cờ
def computer_reply(screen, board):
    # tìm nước đi của máy
    # board: mảng 2 chiều thể hiện trạng thái của bàn cờ
    # return: screen mới cùng board mới
    # position = analyze_current_move(board, -1)
    position = deep_analyze(board)
    drawO(screen, position[1], position[2])
    board[position[1]][position[2]] = -1
    pass
