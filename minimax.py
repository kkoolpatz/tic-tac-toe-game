
import copy

class Counter():
    def __init__(self, start = -1, step = 1):
        self.start = start
        self.step = step

    def count(self):
        while True:
            self.start += 1
            yield self.start


counter = Counter()
board_id = Counter(start = 0)
scorecard = {
    1: [],
    2: [],
    3: [],
    4: [],
    5: [],
    6: [],
    7: [],
    8: [],
    9: [],
    10: [],
}


safe_options = set()

def is_game_over(board):
    
    for row in range(0, 3):
        if (board[row][0] == board[row][1] == board[row][2]) and board[row][2] != "":
            # Game has ended 
            return board[row][0]

        if (board[0][row] == board[1][row] == board[2][row]) and board[2][row] != "":
            # Game has ended
            return board[0][row]

    if (board[0][0] == board[1][1] == board[2][2]) and board[1][1] != "":
        # Game has ended
        return board[0][0]

    if (board[0][2] == board[1][1] == board[2][0]) and board[1][1] != "":
        # Game has ended
        return board[0][2]

    if "" not in board[0] + board[1] + board[2]:
        # Game tied
        return "-"
    
    # Game still active
    return None


def print_board(board, level, counter, score, board_id, best_move):
    pass
    # if score != -1:
    #     print(
    #         "board_id: ", board_id,
    #         "parent: ", counter,
    #         "level: ", level,
    #         "score: ", score,
    #         "best move: ", best_move,
    #     )
    #     for row in range(0, 3):
    #         print(end="|")
    #         for col in range(0, 3):
    #             if board[row][col] == "":
    #                 print (" ", end="|",)
    #             else:
    #                 print(board[row][col], end="|")
    #         print()
    #     print("======\n")



def minimax(board, turn, level):
    
    global counter
    global board_id
    global scorecard
    global safe_options
    this_counter = next(counter.count())
    # print("DEBUG counter: ", this_counter)
    result = is_game_over(board)
    if result is not None:
        if result == "X":
            # print_board(new_board, level, this_counter)
            print("game over X won.")
            return -1
        elif result == "-":
            print("game tied: ")
            return 0
        elif result == "O":
            print("game over O won: ")
            return 1
    print("game is not over.")

    if turn == "X":
        best_score = 111110
    if turn == "O":
        best_score = -111110
    best_move = None

    for row in range(0, 3):
        for col in range(0, 3):
            if board[row][col] == "":
                print("level:", level,turn,"played, row: ", row, ", col: ", col)
                new_board = copy.deepcopy(board)
                new_board[row][col] = turn
                
                if turn  == "X":
                    new_turn = "O"
                else:
                    new_turn = "X"
                new_level = level + 1
            
                # print("game is not over : ", turn, "played: ", row, col)
                this_board_id = next(board_id.count())
                # print("DEBUG this_board_id: ", this_board_id)
                score =  minimax(new_board, new_turn, new_level)
                
                # ###########################
                # if this_counter == 11:
                #     print("#####################################")
                #     print("parent id 11 debug info")
                #     print("turn is:", turn)
                #     print("new_turn is:", new_turn)
                #     print("the current board is:", this_board_id)
                #     print("the current score is:", score)
                #     print("the best score is   :", best_score)
                #     print_board(new_board, new_level, this_counter, score, this_board_id, best_move)
                #     # print("#####################################")
                # ###########################

                # if this_board_id == 11:
                #     print("#####################################")
                #     print("board_id 11 debug info")
                #     print("turn is:", turn)
                #     print("new_turn is:", new_turn)
                #     print("the current board is:", this_board_id)
                #     print("the current score is:", score)
                #     print("the best score is   :", best_score)
                #     print_board(new_board, new_level, this_counter,
                #                 score, this_board_id, best_move)
                #     print("#####################################")
                # ###########################

                if turn == "O":
                    # the score returned is from "O"
                    # This means lower is to be passed forward

                    if score > best_score:
                        best_score = max(best_score, score)
                        best_move = (row, col)
                    else:
                        print("move: ", (row, col), "score:",
                              score, "Not selected as best move")

                if turn == "X":
                    # the score returned is from "O"
                    # This means lower is to be passed forward
                    if score < best_score:
                        best_score = min(best_score, score)
                        best_move = (row, col)
                
                scorecard[new_level].append((score, row, col))

                               
                # if score > best_score:
                best_move = (row, col)
                print_board(new_board, new_level, this_counter, score, this_board_id, best_move)

                    # best_score = score
                # else: 
                    # print_board(new_board, new_level, this_counter, score, this_board_id, best_move)
        
    if best_move is not None:
    
        # print("level: ", level, "best score: ", best_score, "best_move: ", best_move )
        # if score > 1:
        #     print("Best_move and score: ", best_move, score)
        # return score
        return best_score
    else:
        return -200


def impossible_ai(board):

    global counter
    global board_id
    this_counter = next(counter.count())
    
    turn = "O"
    best_score = -111110
    
    best_move = None

    for row in range(0, 3):
        for col in range(0, 3):
            if board[row][col] == "":
                print("level:", 0,turn,"played, row: ", row, ", col: ", col)
                new_board = copy.deepcopy(board)
                new_board[row][col] = turn

                if turn == "X":
                    new_turn = "O"
                else:
                    new_turn = "X"

                # print("game is not over : ", turn, "played: ", row, col)
                this_board_id = next(board_id.count())
                # print("DEBUG this_board_id: ", this_board_id)
                score = minimax(new_board, new_turn, 1)

                if turn == "O":
                    # the score returned is from "O"
                    # This means lower is to be passed forward

                    if score > best_score:
                        best_score = max(best_score, score)
                        best_move = (row, col)
                    else: 
                        print("move: ", (row, col), "score:", score, "Not selected as best move")

                if turn == "X":
                    # the score returned is from "O"
                    # This means lower is to be passed forward
                    if score < best_score:
                        best_score = min(best_score, score)
                        best_move = (row, col)

                print_board(board, 0, this_counter, score, this_board_id, (row, col))

    if best_move is not None:
        print("played: best move ", best_move, "score:", best_score)
        return best_move

    else: 
        print("XXXXXXXX  Something went wrong !!!!  XXXXXXXX")
        print("move ", best_move, "score:", best_score)
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

    # print("Best Move: ", next_move)
    global scorecard
    global safe_options

    for level in [1,2,3]:
        if scorecard[level] != []:
            print ("\n####", level)
            for move in scorecard[level]:
                print(move)
                if level == 1 and move[0] == 1:
                    print("played: winning move ", move[1:2])
                    return move[1:2]
                if level == 1 and move[0] != -1:
                    safe_options.add(move)

    print("\n\n###  Safe options:")
    for move in safe_options:
        print(move)

    pop = safe_options.pop()
    print("played: safe move ", pop[1:3])
    return pop[1:3]

def main():
    
    board = [
        ["X", "X", "O"],
        ["X", "O", "X"],
        ["O", "O", "X"],
    ]


    impossible_ai(board)

if __name__ == "__main__":
    main()
