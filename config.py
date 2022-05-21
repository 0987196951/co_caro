# screen config

# from main import *

screen_size = (400, 400)
screen_color = (160, 160, 160)

# board config
# 0 = ô đang trống, 1 = X, -1 = O

border_thickness = 1
square_size = 40

# tic-tac config

X_color = (0, 0, 128)
O_color = (255,0,0)
tic_tac_thickness = 6
from_border = 9

# analyze points
connect_multiple_four1 = 1e9 + 500
connect_four_has_obstacles1 = 500
connect_four1 = 1e9
connect_multiple_three1 =  1e7
connect_three_has_obstacles1 = 400
connect_three1 = 5000
connect_multiple_two1 = 300
connect_two_has_obstacles1 = 50
connect_two1 = 200

connect_multiple_four2 = 1e8
connect_four_has_obstacles2 = 500
connect_four2 = 1e9
connect_multiple_three2 =  1e6
connect_three_has_obstacles2 = 400
connect_three2 = 1e6
connect_multiple_two2 = 10
connect_two_has_obstacles2 = 2
connect_two2 = 5

#sample
four_in_row_solid = [1, 1, 1, 1]
four_in_row_athwart = [1, 0, 1, 1 ,1]
four_in_row_athwart_reverse = [1, 1, 1, 0, 1]
four_in_row_symmetry = [1, 1, 0, 1, 1]
three_in_row_solid = [1, 1, 1]
three_in_row_athwart = [1, 0, 1, 1]
three_in_row_athwart_reverse = [1, 1, 0, 1]
two_in_row_solid = [1, 1]
two_in_row_symmetry = [1, 0, 1]

#point sample
point_four_in_row_solid = 1e12
point_four_in_row_athwart = 1e5
point_four_in_row_symmetry = 1e5
point_three_in_row_solid = 1e3
point_three_in_row_athwart = 5e2
point_two_row_solid = 100
point_two_row_symmetry = 150

point_four_in_row_obstacles = 5e3
point_three_in_row_obstacles = 100
point_two_in_row_obstacles = 5
point_one_in_row_obstacles = 1

list_sample = [four_in_row_solid, four_in_row_athwart, four_in_row_athwart_reverse, four_in_row_symmetry,
                    three_in_row_solid, three_in_row_athwart, three_in_row_athwart_reverse, two_in_row_solid, two_in_row_symmetry]
point_sample = [1e12, 1e5, 1e5, 1e3, 5e2, 100, 75, 5e3, 100, 5, 1]
dict = {
    'connect_multiple_four1' : connect_multiple_four1,
    'connect_four_has_obstacles1' : connect_four_has_obstacles1,
    'connect_four1' : connect_four1,
    'connect_multiple_three1' :  connect_multiple_three1,
    'connect_three_has_obstacles1' : connect_three_has_obstacles1,
    'connect_three1' : connect_three1,
    'connect_multiple_two1' : connect_multiple_two1,
    'connect_two_has_obstacles1' : connect_two_has_obstacles1,
    'connect_two1' : connect_two1,

    'connect_multiple_four2' : connect_multiple_four2,
    'connect_four_has_obstacles2' : connect_four_has_obstacles2,
    'connect_four2' : connect_four2,
    'connect_multiple_three2' :  connect_multiple_three2,
    'connect_three_has_obstacles2' : connect_three_has_obstacles2,
    'connect_three2' : connect_three2,
    'connect_multiple_two2' : connect_multiple_two2,
    'connect_two_has_obstacles2' : connect_two_has_obstacles2,
    'connect_two2' : connect_two2,

    'point_four_in_row_solid' : point_four_in_row_solid,
    'point_four_in_row_athwart' : point_four_in_row_athwart,
    'point_four_in_row_symmetry' : point_four_in_row_symmetry,
    'point_three_in_row_solid' : point_three_in_row_solid,
    'point_three_in_row_athwart' : point_three_in_row_athwart,
    'point_two_row_solid' : point_two_row_solid,
    'point_two_row_symmetry' : point_two_row_symmetry,

    'point_4_in_row_obstacles' : point_four_in_row_obstacles,
    'point_3_in_row_obstacles' : point_three_in_row_obstacles,
    'point_2_in_row_obstacles' : point_two_in_row_obstacles,
    'point_1_in_row_obstacles' : point_one_in_row_obstacles
}

# text config
win_text1 = "Congratulations! "
win_text2 = " win."
lose_text = " lost."
# win_text = "Congratulations! You win."
# lose_text = "You lost. Try Again?"
text_size = 30
text_color = (249, 248, 113)
text_font = 'freesansbold.ttf'