
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
    global safe_options
    this_counter = next(counter.count())
    # print("DEBUG counter: ", this_counter)
    result = is_game_over(board)
    if result is not None:
        if result == "X":
            # print_board(new_board, level, this_counter)
            # print("game over X won.")
            return -1
        elif result == "-":
            # print("game tied: ")
            return 0
        elif result == "O":
            # print("game over O won: ")
            return 1
    # print("game is not over.")

    if turn == "X":
        best_score = 111110
    if turn == "O":
        best_score = -111110

    for row in range(0, 3):
        for col in range(0, 3):
            if board[row][col] == "":
                # print("level:", level,turn,"played, row: ", row, ", col: ", col)
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
              
                if turn == "O":
                    # the score returned is from "O"
                    # This means higher is to be passed forward

                    if score > best_score:
                        best_score = max(best_score, score)
                        best_move = (row, col)
                    # else:
                    #     print("move: ", (row, col), "score:",
                    #           score, "Not selected as best move")

                if turn == "X":
                    # the score returned is from "X"
                    # This means lower is to be passed forward
                    if score < best_score:
                        best_score = min(best_score, score)

    return best_score

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
                # print("level:", 0,turn,"played, row: ", row, ", col: ", col)
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
                    # else: 
                        # print("move: ", (row, col), "score:", score, "Not selected as best move")

                if turn == "X":
                    # the score returned is from "O"
                    # This means lower is to be passed forward
                    if score < best_score:
                        best_score = min(best_score, score)
                        best_move = (row, col)

                # print_board(board, 0, this_counter, score, this_board_id, (row, col))

    
    # print("played: best move ", best_move, "score:", best_score)
    return best_move


def main():
    
    board = [
        ["X", "X", "O"],
        ["X", "O", "X"],
        ["O", "O", "X"],
    ]


    impossible_ai(board)

if __name__ == "__main__":
    main()
