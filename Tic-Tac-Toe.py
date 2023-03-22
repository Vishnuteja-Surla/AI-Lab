board = [['-']*3]*3

player = 'X'
computer = 'O'
empty_space = '-'

WIN = 999
DRAW = 0
LOSE = -999

win_states = [  #Rows
                [[0,0], [0,1], [0,2]],
                [[1,0], [1,1], [1,2]],
                [[2,0], [2,1], [2,2]],
                #Columns
                [[0,0], [1,0], [2,0]],
                [[0,1], [1,1], [2,1]],
                [[0,2], [1,2], [2,2]],
                #Diagonals
                [[0,0], [1,1], [2,2]],
                [[0,2], [1,1], [2,0]]
            ]


def get_remaining_moves(board):
    moves_left = []
    for i in range(3):
        for j in range(3):
            if board[i][j] != player and board[i][j] != computer:
                moves_left.append([i,j])
                
    return moves_left
    
def filled_pos(board, pos):
    moves_left = get_remaining_moves(board)
    for i in range(len(moves_left)):
        if pos[0] == moves_left[i][0] and pos[1] == moves_left[i][1]:
            return False
    return True

def board_full(board):
    moves_left = get_remaining_moves(board)
    if len(moves_left) == 0:
        return True
    else:
        return False
        

def get_filled_boxes(board, symbol):
    filled_boxes = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == symbol:
                filled_boxes.append([i,j])
    return filled_boxes
    
def game_win(filled_boxes):
    game = True
    for i in range(len(win_states)):
        game = True
        current_win_state = win_states[i]
        for j in range(3):
            if not (filled_boxes.index(current_win_state) != filled_boxes[-1]):
                game = False
                break
        if game:
            break
    return game
    


def board_state(board, marker):
    
    if marker == player:
        non_marker = computer
    else:
        non_marker = player
    
    filled_boxes = get_filled_boxes(board, marker)
    won = game_win(filled_boxes)
    if won:
        return WIN
    filled_boxes = get_filled_boxes(board, non_marker)
    lost = game_win(filled_boxes)
    if lost:
        return LOSE
    if board_full(board):
        return DRAW
    return DRAW


def game_end(board):
    if board_full(board):
        return True
    if DRAW != board_state(board, computer):
        return True
        
    return False
    
def alpha_beta_pruning(board, marker, depth, alpha, beta):
    best_move = [-1, -1]
    if marker == computer:
        best_score = LOSE
    else:
        best_score = WIN
    
    if board_full(board) or DRAW != board_state(board, computer):
        best_score = board_state(board, computer)
        return [best_score, best_move]
    
    moves_left = get_remaining_moves(board)
    
    for i in range(len(moves_left)):
        current_move = moves_left[i]
        if marker == computer:
            score = alpha_beta_pruning(board, player, depth+1, alpha, beta)[0]
            if best_score < score:
                best_score = score - depth * 10
                best_move = current_move
                alpha = max(alpha, best_score)
                board[current_move[0]][current_move[1]] = empty_space
                if beta <= alpha:
                    break
        else:
            score = alpha_beta_pruning(board, computer, depth+1, alpha, beta)[0]
            if best_score > score:
                best_score = score + depth * 10
                best_move = current_move
                beta = min(beta, best_score)
                board[current_move[0]][current_move[1]] = empty_space
                if beta <= alpha:
                    break
        board[current_move[0]][current_move[1]] = empty_space
    return [best_score, best_move] 

def print_board(board):
    for i in board:
        print(i)
        
def get_game_state(state):
    if state == WIN:
        return "WIN"
    if state == LOSE:
        return "LOSE"
    if state == DRAW:
        return "DRAW"

if __name__=='__main__':
    
    print("Your Symbol : X")
    
    print_board(board)
    
    while not game_end(board):
        pos = []
        row = int(input("Enter the row number of your choice : "))
        col = int(input("Enter the column number of your choice : "))
        pos.append(row)
        pos.append(col)
        if filled_pos(board, pos):
            print("Position taken, pick some other position")
        else:
            board[row][col] = player
        ai_move = alpha_beta_pruning(board, 0, -999, 999)
        board[ai_move[1][0]][ai_move[1][1]] = computer
        print(board)
    
    print('<--- GAME OVER --->')
    
    player_state = board_state(board, player)
    game_state = get_game_state(player_state)
    print(game_state)