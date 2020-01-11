

from time import sleep
import sys

def print_grid(game_grid):
    for row in range(0, 3):
        for col in range(0, 3):
            if game_grid[row][col] == "":
                print(" ", end="|")
            else:
                print(game_grid[row][col], end="|")
        print()

def locate_index_pos(mylist, elem):
    
    result = [ i for i in range(0,len(mylist)) if mylist[i] == elem ]
    print("locate index called:", mylist, "Result: ", result)
    return result

def most_repeated(mylist):
    mydict = dict()
    max_count = 0
    max_item = None
    for item in mylist:
        if item in mydict:
            mydict[item] += 1
        else:
            mydict[item] = 1
        if mydict[item] > max_count:
            max_count = mydict[item]
            max_item = item
    
    return max_item, max_count


def dumb_01(game_grid):
    ''' Clicks the first available spot '''
    print("entered dumb_01")
    for row in range(0,3):
        for col in range(0, 3):
            if game_grid[row][col] == "":
                print("dumb_01 returned:", row, col)
                return (row, col)


def dumb_02(game_grid):

    # This AI will try to win or avoid loss. 
    # But cannot think forward. 

    # Assume
    human = "X"
    me = "O"
    to_win = list()
    avoid_loss = list()
    look_ahead_win = list()
    look_ahead_loss = list()
    row = None
    col = None
    # I am winning?
    print("entered dumb_02")
    for unit in range(0,3):

        row = unit
        print("dumb_02 looping row:", row)
        if game_grid[row].count("") == 1:
            print("dumb_02 there is a blank in row:", row)
            # This row is available to play
            if game_grid[row].count(me) == 2:
                # There are two of me
                col = game_grid[row].index("")
                print("dumb_02 is winning (by row):", row, col)
                to_win.append((row, col))  # Win
            if game_grid[row].count(human) == 2:
                # There are two of human
                col = game_grid[row].index("")
                print("dumb_02 is trying to survive (by row):", row, col)
                avoid_loss.append((row, col))  # avoid losing

        if game_grid[row].count("") == 2:
            print("dumb_02 there two blanks in row:", row," :: ",game_grid[row])
            # This row is available to play
            if game_grid[row].count(me) == 1:
                # I already have presense here
                for col in locate_index_pos(game_grid[row], ""):
                    print("dumb_02 look_ahead_win (by row):", row, col)
                    look_ahead_win.append((row, col))  # look Ahead Win
            if game_grid[row].count(human) == 1:
                # Other player already have presense here
                print("dumb_02: Other player already have presense here")
                for col in locate_index_pos(game_grid[row], ""):
                    print("dumb_02 look_ahead_loss (by row):", row, col)
                    look_ahead_loss.append((row, col))  # look Ahead loss


        row = "row done" # Reset
        col = "row donw"  # Reset
    
        # check columns for vertical scan
        col = unit
        print("dumb_02 looping cols:")
        this_col = [game_grid[0][col], game_grid[1][col], game_grid[2][col]]
        if this_col.count("") == 1:
            print("dumb_02 there is a blank in col:", col)
            # This column is available to play
            if this_col.count(me) == 2:
                # There are two of me
                row = this_col.index("")
                print("dumb_02 is winning:", row, col)
                to_win.append((row, col))  # Win
            if this_col.count(human) == 2:
                # There are two of human
                row = this_col.index("")
                print("dumb_02 is trying to survive:", row, col)
                avoid_loss.append((row, col))  # avoid losing

        if this_col.count("") == 2:
            print("dumb_02 there two blanks in col:", col," :: ",this_col)
            # This col is available to play
            if this_col.count(me) == 1:
                # I already have presense here
                for row in locate_index_pos(this_col, ""):
                    print("dumb_02 look_ahead_win (by col):", row, col)
                    look_ahead_win.append((row, col))  # look Ahead Win
            if this_col.count(human) == 1:
                # Other player already have presense here
                print("dumb_02: Other player already have presense here")
                for row in locate_index_pos(this_col, ""):
                    print("dumb_02 look_ahead_loss (by col):", row, col)
                    look_ahead_loss.append((row, col))  # look Ahead loss

        col = None  # Reset

        row = "col done"  # Reset
        col = "col donw"  # Reset

    this_diag = [ game_grid[0][0], game_grid[1][1], game_grid[2][2]]
    print("dumb_02 looping zig diag:", this_diag)
    if this_diag.count("") == 1:
        # This diag is available to play
        if this_diag.count(me) == 2:
            # There are two of me
            row = this_diag.index("")
            col = this_diag.index("")
            print("dumb_02 is winninh via zig:", row, col)
            to_win.append((row, col))  # Win
        if this_diag.count(human) == 2:
            # There are two of human
            row = this_diag.index("")
            col = this_diag.index("")
            print("dumb_02 is trying to survive via zig:", row, col)
            avoid_loss.append((row, col))  # avoid losing

    if this_diag.count("") == 2:
        # This diag is available to play
        if this_diag.count(me) == 1:
            # I already have presense here
            for row in locate_index_pos(this_diag, ""):
                col = row
                print("dumb_02 look_ahead_win via zig:", row, col)
                look_ahead_win.append((row, col))  # look Ahead Win

        if this_diag.count(human) == 1:
            # Other player already have presense here
            for row in locate_index_pos(this_diag, ""):
                col = row
                print("dumb_02 look_ahead_loss via zig:", row, col)
                look_ahead_loss.append((row, col))  # look Ahead Loss


    this_diag = [game_grid[0][2], game_grid[1][1], game_grid[2][0]]
    print("dumb_02 looping zag diag:", this_diag)
    if this_diag.count("") == 1:
        print("dumb_02 there is a blank in zag:", this_diag)
        # This diag is available to play
        if this_diag.count(me) == 2:
            # There are two of me
            row = this_diag.index("")
            col = 2 - row
            print("dumb_02 is winning:", row, col)
            to_win.append((row, col))  # Win
        if this_diag.count(human) == 2:
            # There are two of human
            row = this_diag.index("")
            col = 2 - row
            print("dumb_02 is trying to survive:", row, col)
            avoid_loss.append((row, col))  # avoid losing
    
    if this_diag.count("") == 2:
        # This diag is available to play
        if this_diag.count(me) == 1:
            # I already have presense here
            for row in locate_index_pos(this_diag, ""):
                col = 2 - row
                print("dumb_02 look_ahead_win via zag:", row, col)
                look_ahead_win.append((row, col))  # look Ahead Win

        if this_diag.count(human) == 1:
            # Other player already have presense here
            for row in locate_index_pos(this_diag, ""):
                col = 2 - row
                print("dumb_02 look_ahead_loss via zag:", row, col)
                look_ahead_loss.append((row, col))  # look Ahead Loss

    for row, col in [(0, 0), (0, 2), (2, 0), (2, 2)]:
        if game_grid[row][col] == human:
            if game_grid[2-row][2-col] == "":
                print("dumb_02: look ahead win ( capture opp corner algo) ", 2-row, 2-col)
                print("dumb_02: look ahead loss ( capture opp corner algo) ", 2-row, 2-col)
                look_ahead_loss.append((2-row, 2-col))  # look Ahead Loss
                look_ahead_win.append((2-row, 2-col))  # look Ahead win

    if game_grid[1][1] == "":
        print("dumb_02: look ahead win (middle algo) ", 1, 1)
        print("dumb_02: look ahead loss (middle algo) ", 1, 1)
        look_ahead_loss.append((1, 1))  # look Ahead Loss
        look_ahead_win.append((1, 1))  # look Ahead Loss
    else:
        for row, col in [(0, 0), (0, 2), (2, 0), (2, 2) ]:
            if game_grid[row][col] == "":
                print("dumb_02: look ahead win (corner algo) ", row, col)        
                look_ahead_loss.append((row, col))  # look Ahead Loss
                look_ahead_win.append((row, col))  # look Ahead win


    if len(to_win) > 0:
        print("Chose Winning move:", to_win[0])
        return to_win[0] # win

    if len(avoid_loss) > 0:
        print("Chose Saving move:", avoid_loss[0])
        return avoid_loss[0]  # avoid_loss

    print("dumb_02 No win or loss this turn")
    print("looking at win or loss next turn")

    if len(look_ahead_win) > 0:
        
        win_ahead_move, win_ahead_weight = most_repeated(look_ahead_win)
        # return most_repeated(look_ahead_win)
    else:
        win_ahead_weight = 0
        print("dumb_02: look_ahead_win is empty")


    if len(look_ahead_loss) > 0:
        loss_ahead_move, loss_ahead_weight = most_repeated(look_ahead_loss)
        # return most_repeated(look_ahead_loss)
    else:
        loss_ahead_weight = 0
        print("dumb_02: look_ahead_loss is empty")

    print("dumb_02: win_ahead_weight:", win_ahead_weight)
    print("dumb_02: loss_ahead_weight:", loss_ahead_weight)

    if win_ahead_weight > 0:
        if win_ahead_weight >= loss_ahead_weight:
            print("Playing win_ahead_move")
            return win_ahead_move
    if loss_ahead_weight > 0:
        print("Playing loss_ahead_move")
        return loss_ahead_move



    print("No win or loss next turn")

    # Corner fight algo
    for row in [0, 2]:
        for col in [0, 2]:
            if game_grid[row][col] == human:
                test_row, test_col = 2 - row, 2 - col
                if game_grid[test_row][test_col] == "":
                    print("dumb_02 exec corner fight algo:", test_row, test_col)
                    row, col  = test_row, test_col
                    return (row, col)

    if game_grid[1][1] == "":
        print("dumb_02: exec middle algo")
        return (1,1)

    for row in [0, 2]:
        for col in [0, 2]:
            if game_grid[row][col] == "":
                print("dumb_02 exec corner algo:", row, col)
                return (row, col)
    
    for row, col in [[0, 1], [1, 0], [1, 2], [2, 1]]:
        if game_grid[row][col] == "":
            print("dumb_02 exec central edge algo:", row, col)
            return (row, col)
    
    print("dumb_02: code should never reach here")
    print("something is really wrong")
    print_grid(game_grid)
    sys.exit()

