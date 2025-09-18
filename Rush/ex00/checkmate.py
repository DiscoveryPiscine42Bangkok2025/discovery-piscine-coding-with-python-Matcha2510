def checkmate(board_str):
   
    #Parse the board into a 2-D list 
    board = [list(line) for line in board_str.strip().splitlines()]
    n = len(board)

    #locate King
    king_pos = None
    for r in range(n):
        for c in range(len(board[r])):
            if board[r][c] == 'K':
                king_pos = (r, c)
                break
        if king_pos:
            break
    if not king_pos:
        print("Fail")
        return

    kr, kc = king_pos

    def on_board(r, c):
        return 0 <= r < n and 0 <= c < len(board[r])

    #check functions for each piece
    def check_pawn():
        for dr, dc in [(1, -1), (1, 1)]:
            r, c = kr + dr, kc + dc
            if on_board(r, c) and board[r][c] == 'P':
                return True
        return False

    def check_dirs(directions, symbols):
        #for rooks, bishops, queens: slide in each direction
        for dr, dc in directions:
            r, c = kr + dr, kc + dc
            while on_board(r, c):
                cell = board[r][c]
                if cell != '.':
                    if cell in symbols:
                        return True
                    break
                r += dr
                c += dc
        return False

    #bishop or queen diagonals
    def check_bishop_queen():
        dirs = [(-1,-1),(-1,1),(1,-1),(1,1)]
        return check_dirs(dirs, {'B','Q'})

    #rook or queen orthogonals
    def check_rook_queen():
        dirs = [(-1,0),(1,0),(0,-1),(0,1)]
        return check_dirs(dirs, {'R','Q'})

    #Evaluate threats
    in_check = (
        check_pawn() or
        check_bishop_queen() or
        check_rook_queen()
    )

    print("Success" if in_check else "Fail")
