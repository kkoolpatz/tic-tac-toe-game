from p5 import *
from time import sleep
from ai import *
from minimax import impossible_ai
import sys

modes = ["2H", "HC", "2C"]
mode = "HC"
# mode = "2H"
grid_size = 700
text_area = 200
cell = grid_size/3
unit = cell/4
section = [cell, cell*2, grid_size]

# Global Variables that are reset in init
is_x = None
is_human = None
game_grid = None
game_restart = None
game_restart_logged = None
init_view = True
run_once = True
bg = Color(255, 255, 255, 255)
def init():

    global is_x
    global is_human
    global game_grid
    global game_restart
    global game_restart_logged

    is_x = True
    is_human = True
    game_restart = False
    game_restart_logged = False

    game_grid = [
        ["", "", ""],
        ["", "", ""],
        ["", "", ""],
    ]
    new_move_banner()


def setup():
    
    print(">>>>>>> New Game <<<<<<<")
    init()
    global grid_size
    global bg
    background(bg)
    size(grid_size, grid_size + text_area)
    

    
def draw():
    global section
    global grid_size
    global run_once
    global bg
    
    if run_once:
        background(bg)
        run_once = not run_once
    f = create_font("/home/patz/.config/google-chrome/Default/Extensions/pioclpoplcdbaefihamjohnefbikjilc/7.12.3_0/res/range-mono-medium.ttf", size = 20)
    text_font(f)
    fill(125)
    stroke_weight(8)
    square((unit, grid_size + unit), unit*2)
    square((unit*5, grid_size + unit), unit*2)
    fill(0)
    text("HvC",(unit * 1.6, grid_size + (unit*1.7)))
    text("HvH", (unit * 5.6, grid_size + (unit*1.7)))
    fill(255)
    line((0, 4), (grid_size, 4)) # Top line
    line((4, 0), (4, grid_size)) # Left
    line((section[0], 0), (section[0], section[2])) # Mid vertical 1
    line((section[1], 0), (section[1], section[2]))  # Mid vertical 2
    line((0, section[0]), (section[2], section[0]))  # Mid horizontal 1
    line((0, section[1]), (section[2], section[1]))  # Mid horizontal 2
    line((grid_size - 4, 0), (grid_size - 4, grid_size)) # right line 
    line((0, grid_size), (grid_size, grid_size )) # Bottom line
    # fill(10, 102, 153, 255)
    # text("New Game!", (30, grid_size + 100))
    
    if not is_human:
        # sleep(0.5) # To simulate delay
        autoplay()
    

def autoplay():
    global game_grid
    global game_restart
    global game_restart_logged

    if game_restart:
        if game_restart_logged:
            return

        game_restart_logged = True
        print("Game has ended. Computer waiting for human to reset")
        return

    row, col = dumb_02(game_grid)
    # row, col = impossible_ai(game_grid)

    play_turn(row, col)

def mouse_clicked():
    global mouse_x
    global mouse_y
    global cell
    global game_restart
    global init_view
    global mode
    # print(">>>>>> Mouse Clicked:", mouse_x, mouse_y)
        
    if (
        mouse_x >= unit
        and mouse_x <= unit * 3 
        and mouse_y >= grid_size + unit
        and mouse_y <= grid_size + (unit * 3)
    ):
        print("Restarting Game: Human Vs Computer")
        mode = "HC"
        setup()

    if (
        mouse_x >= unit * 5
        and mouse_x <= unit * 7
        and mouse_y >= grid_size + unit
        and mouse_y <= grid_size + (unit * 3)
    ):
        print("Restarting Game: Human Vs Human")
        mode = "2H"
        setup()

    # else:
    #     print("mouse_x expected between:", 
    #             unit, "and", unit * 3, "recvd:",  mouse_x)
        
    #     print("mouse_y expected between:",
    #             grid_size + unit, "and", grid_size + (unit * 3),
    #             "recvd:",  mouse_y)
        
    # square((unit*5, grid_size + unit), unit*2)

    if game_restart:
        setup()
        return

    if not is_human:
        print("mouse clicked out of turn, wait for computer to play")
        return

        

    row = int(mouse_y / cell)
    col = int(mouse_x / cell)

    play_turn(row, col)


def play_turn(row, col):
    global is_x
    global is_human
    global game_grid

    if row > 2 or col > 2:
        return

    if game_grid[row][col] == "":
        if is_x:
            draw_x(row, col)
            game_grid[row][col] = "X"
        else:
            draw_o(row, col)
            game_grid[row][col] = "O"

        if is_human:
            print("human played: ", row, col)
        else:
            print("computer played: ", row, col)
        has_game_ended()
        is_x = not is_x
        #print("X toggled")
        if mode == "HC":
            # print("human vs computer toggled")
            is_human = not is_human
            new_move_banner()

    else:
        print("incorrect square")


def draw_x(row, col):
    global unit
    
    stroke_weight(6)
    stroke("Red")
    point_1 = (section[col] - unit*3, section[row] - unit*3)
    point_2 = (section[col] - unit*1, section[row] - unit*1)
    line(point_1, point_2)

    point_1 = (section[col] - unit*1, section[row] - unit*3)
    point_2 = (section[col] - unit*3, section[row] - unit*1)
    line(point_1, point_2)

def draw_o(row, col):
    global unit
    global game_grid
    stroke("Blue")
    # fill("Blue")
    stroke_weight(6)
    center = (section[col] - unit*2, section[row] - unit*2)
    circle(center, unit*2)
    

def wait_init_mode():
    global init_view
    return init_view

def has_game_ended():
    global game_grid
    global game_restart
    global grid_size
    stroke_weight(50)
    near_edge = 3.25
    far_edge = 0.75
    stroke(0,120,0,180)
    for row in range(0,3):
        if (game_grid[row][0] == game_grid[row][1] == game_grid[row][2]) and game_grid[row][2] != "":
            print("gameover row")        
            point_1 = (section[0] - unit*near_edge, section[row] - unit*2)
            point_2 = (section[2] - unit*far_edge, section[row] - unit*2)
            line(point_1, point_2)
            game_restart = True
            
        if (game_grid[0][row] == game_grid[1][row] == game_grid[2][row]) and game_grid[2][row] != "":
            print("gameover col")
            point_1 = (section[row] - unit*2, section[0] - unit*near_edge)
            point_2 = (section[row] - unit*2, section[2] - unit*far_edge)
            line(point_1, point_2)
            game_restart = True
        
    if (game_grid[0][0] == game_grid[1][1] == game_grid[2][2]) and game_grid[1][1] != "":
            print("gameover zig")
            point_1 = (section[0] - unit*near_edge, section[0] - unit*near_edge)
            point_2 = (section[2] - unit*far_edge, section[2] - unit*far_edge)
            line(point_1, point_2)
            game_restart = True

    if (game_grid[0][2] == game_grid[1][1] == game_grid[2][0]) and game_grid[1][1] != "":
            print("gameover zag")
            point_1 = (section[2] - unit*far_edge, section[0] - unit*near_edge)
            point_2 = (section[0] - unit*near_edge, section[2] - unit*far_edge)
            line(point_1, point_2)
            game_restart = True
    
    if not game_restart:
        # print("tur finished: game on")
        if "" not in game_grid[0] + game_grid[1] + game_grid[2] :
        
            print("its a tie", game_grid[0] + game_grid[1] + game_grid[2])
            game_restart = True

    stroke(0, 0, 0)

def new_move_banner():
    global is_human
    print("==============================================")
    if is_human:
        print("## human to play")
    else:
        print("## computer to play")
    # print("==============================================")

run()


