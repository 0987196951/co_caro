from email.base64mime import body_encode
from multiprocessing import BoundedSemaphore
from config import *
def not_valid(board, x):
    nboard = len(board)
    if x < 0 or x >= nboard:
        return True
    return False

def coppyList(list):
    nlist = len(list)
    v = [[0 for i in range(nlist)] for i in range(nlist)]
    for i in range(nlist):
        for j in range(nlist):
            v[i][j] = list[i][j]
    return v
def have_five(board, next_player, x, y):
    (up, down, left, right) = (0, 0, 0, 0)
    (up_left, down_left, up_right, down_right) = (0, 0, 0, 0)
    while x - up >= 0 and board[x - up][y] == next_player:
        up += 1
    while x + down < len(board) and board[x + down][y] == next_player:
        down += 1
    while y - left >= 0 and board[x][y - left] == next_player:
        left += 1
    while y + right < len(board) and board[x][y + right] == next_player:
        right += 1
    while x - up_left >= 0 and y - up_left >= 0 and board[x - up_left][y - up_left] == next_player:
        up_left += 1
    while x + down_right < len(board) and y + down_right < len(board) and board[x + down_right][
        y + down_right] == next_player:
        down_right += 1
    while x + down_left < len(board) and y - down_left >= 0 and board[x + down_left][y - down_left] == next_player:
        down_left += 1
    while x - up_right >= 0 and y + up_right < len(board) and board[x - up_right][y + up_right] == next_player:
        up_right += 1
    points = 0
    if up + down - 2 >= 4: return True
    if left + right - 2 >= 4: return True
    if down_left + up_right - 2 >= 4: return True
    if up_left + down_right - 2 >= 4: return True
    return False


def five_in_a_row(board, next_player, x, y):
    return have_five(board, next_player, x, y)

def enemy_five_in_a_row(board, next_player):
    board_size = len(board)
    for i in range(board_size):
        for j in range(board_size):
            if board[i][j] == next_player:
                if five_in_a_row(board, next_player, i, j):
                    return True
    return False
def get_point_horizontal_line(board, x, y, list, k_list, next_player, rank): # check hàng ngang xem có mẫu nào giống trong sample
    scale = 1
    if rank == 2 :
        scale = 0.9
    elif rank == 3 :
        scale = 0.8
    size = len(board)
    list_cur = [next_player * i for i in list]
    for i in range(len(list_cur)) :
        if board[x][y + i] != list_cur[i] :
            return 0
    if (y-1 < 0 or board[x][y-1] == -next_player ) and ( y + len(list) >= size or board[x][y+len(list)] == -next_player )  :
        return 0 # check xem có bị chặn 2 đầu
    if y - 1 >= 0 or y + len(list) < size:
        if board[x][y-1] == -next_player or board[x][y-1] == -next_player: # check xem có cản ở 1 đầu hay ko
            return dict[f'point_{len(list)-1}_in_row_obstacles'] * scale
    return point_sample[k_list] * scale
def get_point_vertical_line(board, x, y, list, k_list, next_player, rank): # check hàng dọc xem có giống với mẫu nào trong sample ko
    scale = 1
    if rank == 2 :
        scale = 0.9
    elif rank == 3 :
        scale = 0.8
    size = len(board)
    list_cur = [next_player * i for i in list]
    for i in range(len(list_cur)) :
        if board[x+i][y] != list_cur[i] :
            return 0
    if (x-1 < 0 or board[x-1][y] == -next_player ) and (x + len(list) >= size or board[x+len(list)][y] == -next_player ) : 
        return 0
    if x - 1 >= 0 or x + len(list) < size:
        if board[x-1][y] == -next_player or board[x+len(list)][y] == -next_player :
            return dict[f'point_{len(list)-1}_in_row_obstacles'] * scale
    return point_sample[k_list] * scale
def get_point_primary_diagonal(board, x, y, list, k_list, next_player, rank): # check với đg chéo chính
    scale = 1
    if rank == 2 :
        scale = 0.9
    elif rank == 3 :
        scale = 0.8
    size = len(board)
    list_cur = [next_player * i for i in list]
    for i in range(len(list_cur)) :
        if board[x+i][y + i] != list_cur[i] :
            return 0
    if (y - 1 < 0 or x - 1 < 0 or board[x-1][y-1] == -next_player) \
        and (x + len(list) >= size or y + len(list) >= size or board[x+len(list)][y+len(list)] == -next_player)  :
            return 0
    if y - 1 >= 0 and x - 1 >= 0 and x + len(list) < size and y + len(list) < size:
        if board[x-1][y-1] == -next_player or board[x+len(list)][y+len(list)] == -next_player :
                return dict[f'point_{len(list)-1}_in_row_obstacles'] * scale
    return point_sample[k_list] * scale
def get_point_extra_diagonal(board, x, y, list, k_list, next_player, rank): # check với đường chéo phụ
    scale = 1
    if rank == 2:
        scale = 0.9
    elif rank == 3 :
        scale = 0.8
    size = len(board)
    list_cur = [next_player * i for i in list]
    for i in range(len(list_cur)) :
        if board[x-i][y + i] != list_cur[i] :
            return 0
    if (x + 1 >= size or y - 1 < 0 or board[x+1][y-1] == -next_player) \
        and (x-len(list) < 0 or y + len(list) >= size or board[x-len(list)][y+len(list)]) :
            return 0
    if y - 1 >= 0 and x + 1 < size:
        if board[x+1][y-1] == -next_player or board[x+1][y-1] == -next_player :
            if board[x+1][y-1] == -next_player and board[x+1][y-1] == -next_player :
                return 0
            else :
                return dict[f'point_{len(list)-1}_in_row_obstacles'] * scale
    return point_sample[k_list] * scale
def process(board: list, next_player: int, x: int, y: int, rank : int):
    size = len(board)
    # while x - up >= 0 and board[x - up][y] == next_player:
    #     up += 1
    # while x + down < len(board) and board[x + down][y] == next_player:
    #     down += 1
    # while y - left >= 0 and board[x][y - left] == next_player:
    #     left += 1
    # while y + right < len(board) and board[x][y + right] == next_player:
    #     right += 1
    # while x - up_left >= 0 and y - up_left >= 0 and board[x - up_left][y - up_left] == next_player:
    #     up_left += 1
    # while x + down_right < len(board) and y + down_right < len(board) and board[x + down_right][
    #     y + down_right] == next_player:
    #     down_right += 1
    # while x + down_left < len(board) and y - down_left >= 0 and board[x + down_left][y - down_left] == next_player:
    #     down_left += 1
    # while x - up_right >= 0 and y + up_right < len(board) and board[x - up_right][y + up_right] == next_player:
    #     up_right += 1
    # points = 0
    # if up + down - 2 >= amount - 1:
    #     if (not_valid(board, x - up) and not_valid(board, x + down)) or (
    #             not_valid(board, x - up) == False and board[x - up][y] == -next_player and
    #             not_valid(board, x + down) == False and board[x + down][y] == -next_player):
    #         pass
    #     elif not_valid(board, x - up) or not_valid(board, x + down) or board[x - up][y] == -next_player or \
    #             board[x + down][y] == -next_player:
    #         points += dict[f'connect_{nums}_has_obstacles{rank}']
    #     else:
    #         points += dict[f'connect_{nums}{rank}']
    # if left + right - 2 >= amount - 1:
    #     if not_valid(board, y - left) and not_valid(board, y + right) or (
    #             not_valid(board, y - left) == False and board[x][y - left] == -next_player and
    #             not_valid(board, y + right) == False and board[x][y + right] == -next_player):
    #         pass
    #     elif not_valid(board, y - left) or not_valid(board, y + right) or board[x][y - left] == -next_player or \
    #             board[x][y + right] == -next_player:
    #         points += dict[f'connect_{nums}_has_obstacles{rank}']
    #     else:
    #         points += dict[f'connect_{nums}{rank}']
    # if up_left + down_right - 2 >= amount - 1:
    #     if (not_valid(board, x - up_left) or not_valid(board, y - up_left)) and (
    #             not_valid(board, x + down_right) or not_valid(board, y + down_right)) \
    #             or (not_valid(board, x - up_left) == False and not_valid(board, y - up_left) == False and
    #                 board[x - up_left][y - up_left] == -next_player and
    #                 not_valid(board, x + down_right) == False and not_valid(board, y + down_right) == False and
    #                 board[x + down_right][y + down_right] == -next_player):
    #         pass
    #     elif not_valid(board, x - up_left) or not_valid(board, y - up_left) or not_valid(board,
    #                                                                                      x + down_right) or not_valid(
    #         board, y + down_right) \
    #             or board[x - up_left][y - up_left] == -next_player or board[x + down_right][
    #         y + down_right] == -next_player:
    #         points += dict[f'connect_{nums}_has_obstacles{rank}']
    #     else:
    #         points += dict[f'connect_{nums}{rank}']
    # if up_right + down_left - 2 >= amount - 1:
    #     if (not_valid(board, x - up_right) or not_valid(board, y + up_right)) and (
    #             not_valid(board, x + down_left) or not_valid(board, y - down_left)) \
    #             or (not_valid(board, x - up_right) == False and not_valid(board, y + up_right) == False and
    #                 board[x - up_right][y + up_right] == -next_player
    #                 and not_valid(board, x + down_left) == False and not_valid(board, y - down_left) == False and
    #                 board[x + down_left][y - down_left] == -next_player):
    #         pass
    #     elif (not_valid(board, x - up_right) or not_valid(board, y + up_right)) or (
    #             not_valid(board, x + down_left) or not_valid(board, y - down_left)) \
    #             or (board[x - up_right][y + up_right] == -next_player or board[x + down_left][
    #         y - down_left] == -next_player):
    #         points += dict[f'connect_{nums}_has_obstacles{rank}']
    #     else:
    #         points += dict[f'connect_{nums}{rank}']
    # if points > dict[f'connect_{nums}{rank}']:
    #     return dict[f'connect_multiple_{nums}{rank}'] + points
    # elif points == dict[f'connect_{nums}{rank}']:
    #     return dict[f'connect_{nums}{rank}'] + points
    # elif points > dict[f'connect_{nums}_has_obstacles{rank}']:
    #     return dict[f'connect_{nums}_has_obstacles{rank}'] + points
    # return 0
    points = 0
    for k, list in enumerate(list_sample) : # duyệt qua từng mẫu trong sample 
        for i in range(len(list)) : # check với vị trị x, y từng vị trí với mẫu trong sample
            if x - i >= 0 and x - i + len(list) < size : 
                points += get_point_vertical_line(board, x-i, y, list, k, next_player, rank)
            if y - i >= 0 and y - i + len(list) < size :
                points += get_point_horizontal_line(board, x, y-i, list, k, next_player, rank)
            if x - i >= 0 and x - i + len(list) < size and y - i >= 0 and y - i + len(list) < size :
                points += get_point_primary_diagonal(board, x-i, y - i, list, k, next_player, rank)
            if x + i < size and x + i - len(list) >= 0 and y - i >= 0 and y - i + len(list) < size :
                points += get_point_extra_diagonal(board, x + i, y - i, list, k, next_player, rank)
    return points
def four_in_a_row(board, next_player, x, y, rank):
    return process(board, next_player, x, y, 'four', 4, rank)


def three_in_a_row(board, next_player, x, y, rank):
    return process(board, next_player, x, y, 'three', 3, rank)


def two_in_a_row(board, next_player, x, y, rank):
    return process(board, next_player, x, y, 'two', 2, rank)


def enemy_four_in_a_row(board, next_player):
    board_size = len(board)
    points = (0, 0, 0)
    for i in range(board_size):
        for j in range(board_size):
            if board[i][j] == 0:
                newL = coppyList(board)
                newL[i][j] = next_player
                cur_point = four_in_a_row(newL, next_player, i, j, '2')
                if points[0] < cur_point:
                    points = (cur_point, i, j)
    return points

def enemy_three_in_a_row(board, next_player):
    board_size = len(board)
    points = (0, 0, 0)
    for i in range(board_size):
        for j in range(board_size):
            if board[i][j] == 0:
                newL = coppyList(board)
                newL[i][j] = next_player
                cur_point = three_in_a_row(newL, next_player, i, j, '2')
                if points[0] < cur_point:
                    points = (cur_point, i, j)
    return points

def enemy_two_in_a_row(board, next_player):
    board_size = len(board)
    points = (0, 0, 0)
    for i in range(board_size):
        for j in range(board_size):
            if board[i][j] == 0:
                newL = coppyList(board)
                newL[i][j] = next_player
                cur_point = two_in_a_row(newL, next_player, i, j, '2')
                newL[i][j] = 0
                if points[0] < (cur_point):
                    points = (cur_point, i, j)
    return points
def enemy_max_points(board, nextplayer, rank) : # tính nước đi có số điểm lớn nhất trên bàn cờ
    board_size = len(board)
    points = (0, 0, 0)
    for i in range(board_size):
        for j in range(board_size):
            if board[i][j] == 0:
                newL = coppyList(board)
                newL[i][j] = nextplayer
                cur_point = process(newL, nextplayer, i, j, rank)
                newL[i][j] = 0
                if points[0] < cur_point :
                    points = (cur_point, i, j)
    return points