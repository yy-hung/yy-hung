
import check

##Constants

board1 = [[ '',  '',  '', 'B',  '', 'B', 'W',  ''],
          [ '', 'W',  '',  '', 'W',  '',  '',  ''],
          ['B',  '', 'B',  '',  '', 'B', 'W',  ''],
          [ '',  '',  '',  '',  '',  '', 'W',  ''],
          ['B',  '',  '', 'B',  '',  '', 'B', 'B'],
          [ '', 'W', 'B',  '',  '', 'B',  '', 'W'],
          [ '', 'B',  '',  '', 'W',  '',  '',  ''],
          [ '',  '',  '',  '',  '',  '',  '',  '']]

## A Board is a (listof (listof Str))
## Requires:
##   The length of the outer list is 8.
##   The length of each inner list is 8.
##   Each string is '', 'B', or 'W'.

def same_loc(board, turn, row, col, lst):
    '''
    Returns False if position row, col is not an empty string, otherwise, 
    returnsa list lst of lists of integers which represent the coordinates
    of closest positions of the same turn colour on the left and right of the 
    same row and all other positions on the same column and diagonals of 
    position at row and col on the board
    
    same_loc: (listof (listof Str)) Str Nat Nat Any -> (anyof Bool (listof (list Nat Nat)))
    Requires: as stated on the top, 0 <= row, col <= 7
    
    Examples:       
       same_loc(board1,'B',7,0,[]) => False
       same_loc(board1,'B',0,0,[]) => [[0, 3], [2, 0], [4, 0], [7, 0], [2, 2], [5, 5]]
       same_loc(board1,'W',7,0,[]) => []             
    '''
    lst = []
    if board[row][col] != '':
        return False
    if row == 0: #row 0
        if col == 0: #(0,0)
            if turn in board[0]: #right
                a = board[0].index(turn)
                lst = lst + [[0,a]]
            i = 1
            while i < 8:
                if board[i][0] == turn:
                    lst = lst + [[i,0]] #row
                    i += 1
                else:
                    i += 1
            i = 1
            while i < 8:
                if board[i][i] == turn:
                    lst = lst + [[i,i]] #lower right diag
                    i += 1
                else:
                    i += 1
            return lst
        if col == 7: #(0,7)
            if turn in board[0]: #left
                a = board[0][::-1]
                c = a.index(turn)
                lst = lst + [[0,7 - c]]
            i = 1
            while i < 8:
                if board[i][7] == turn:
                    lst = lst + [[i,7]] #row
                    i += 1
                else:
                    i += 1
            i = 1
            while i < 8:
                if board[i][7 - i] == turn:
                    lst = lst + [[i,7 - i]] #lower left diag
                    i += 1
                else:
                    i += 1
            return lst  
        else: #others in row 0
            if turn in board[0][:col]: #left
                a = board[0][:col][::-1]
                c = a.index(turn)
                lst = lst + [[0,col - c - 1]]
            if turn in board[0][col + 1:]: #right
                a = board[0][col + 1:].index(turn)
                lst = lst + [[0,col + a + 1]]
            i=1
            while i < 8: # row
                if board[i][col]==turn:
                    lst = lst + [[i,col]]
                    i += 1
                else:
                    i += 1
            i = 0
            while i < col:
                if board[col - i][i] == turn:
                    lst = lst + [[col - i,i]] #lower left diag
                    i += 1
                else:
                    i += 1
            i = col + 1
            while i < 8:
                if board[i - col][i] == turn:
                    lst = lst + [[i - col,i]] #lower right diag
                    i += 1
                else:
                    i += 1
            return lst
        
    if row == 7: #row 7
        if col == 0: #(7,0)
            if turn in board[7]: #right
                a = board[7].index(turn)
                lst = lst + [[7,a]]
            i = 0
            while i < 7:
                if board[i][0] == turn:
                    lst = lst + [[i,0]] #row
                    i += 1
                else:
                    i += 1
            i = 1
            while i < 8:
                if board[7 - i][i]==turn:
                    lst = lst + [[7 - i,i]] #upper right diag
                    i += 1
                else:
                    i += 1
            return lst
        if col == 7: #(7,7)
            if turn in board[7]: #left
                a = board[7][::-1]
                c = a.index(turn)
                lst = lst + [[7,7 - c]]
            i = 0
            while i < 7:
                if board[i][7] == turn:
                    lst = lst + [[i,7]] #row
                    i += 1
                else:
                    i += 1
            i = 0
            while i < 7:
                if board[i][i] == turn:
                    lst = lst + [[i,i]] #upper left diag
                    i += 1
                else:
                    i += 1
            return lst  
        else: #others in row 7
            if turn in board[7][:col]: #left
                a = board[7][:col][::-1]
                c = a.index(turn)
                lst = lst + [[7,col - c - 1]]
            if turn in board[7][col + 1:]: #right
                a = board[7][col + 1:].index(turn)
                lst = lst + [[7,col + a + 1]]
            i = 0
            while i < 7: # row
                if board[i][col] == turn:
                    lst = lst + [[i,col]]
                    i += 1
                else:
                    i += 1
            i = 7 - col
            j = 0
            while i < 7:
                if board[i][j] == turn:
                    lst = lst + [[i,j]] #upper left diag
                    i += 1
                    j += 1
                else:
                    i += 1
                    j += 1
            i = col
            j = 7
            while i < 7:
                if board[i][j] == turn:
                    lst = lst + [[i,j]] #upper right diag
                    i += 1
                    j -= 1
                else:
                    i += 1
                    j -= 1
            return lst  
    if col == 0: #col 0 (row1-6)
        if turn in board[row]: #right
            a = board[row].index(turn)
            lst = lst + [[row,a]]
        i = 0
        while i < row:
            if board[i][0]==turn:
                lst = lst + [[i,0]] #up
                i += 1
            else:
                i += 1
        i = row + 1
        while i < 8:
            if board[i][0] == turn:
                lst = lst + [[i,0]] #down
                i += 1
            else:
                i += 1
        i = 0
        j = row
        while i < row:
            if board[i][j] == turn:
                lst = lst + [[i,j]] #upper right diag
                i += 1
                j -= 1
            else:
                i += 1
                j -= 1
        i = row + 1        
        while i < 8:
            if board[i][i - row] == turn:
                lst = lst + [[i,i - row]] #lower right diag
                i += 1
            else:
                i += 1
        return lst 
    if col == 7: #col 7 (row1-6)
        if turn in board[row]: #left
            a = board[row][::-1]
            c = a.index(turn)
            lst = lst + [[row,7 - c]]
        i = 0
        while i < row:
            if board[i][7] == turn:
                lst = lst + [[i,7]] #up
                i += 1
            else:
                i += 1
        i = row + 1
        while i < 8:
            if board[i][7] == turn:
                lst = lst + [[i,7]] #down
                i += 1
            else:
                i += 1
        i = 0  
        j = 7 - row
        while i < row:
            if board[i][j] == turn:
                lst = lst + [[i,j]] #upper left diag
                i += 1
                j += 1
            else:
                i += 1
                j += 1
        i = row + 1
        j = 6
        while i < 8:
            if board[i][j] == turn:
                lst = lst + [[i,j]] #lower left diag
                i += 1
                j -= 1
            else:
                i += 1
                j -= 1
        return lst 
    else: #anything else in the board (row1 - 6,col1 - 6)
        if turn in board[row][:col]: #left
            a = board[row][:col][::-1]
            c = a.index(turn)
            lst = lst + [[row,col - c - 1]]
        if turn in board[row][col + 1:]: #right
            a = board[row][col + 1:].index(turn)
            lst = lst + [[row,col + a + 1]]   
        i = 0
        while i < row:
            if board[i][col] == turn:
                lst = lst + [[i,col]] #up
                i += 1
            else:
                i += 1
        i = row + 1
        while i < 8:
            if board[i][col] == turn:
                lst = lst + [[i,col]] #down
                i += 1
            else:
                i += 1
        total = row + col
        if total <= 7: #upper right&lower left diag-reaches row 0
            i = 0
            while i < row:
                if board[i][total - i] == turn:
                    lst = lst + [[i,total - i]] 
                    i += 1
                else:
                    i += 1
            i = total
            j = 0
            while i > row:
                if board[i][j] == turn:
                    lst = lst + [[i,j]] 
                    i -= 1
                    j += 1
                else:
                    i -= 1   
                    j += 1                   
        if total > 7:   #upper right&lower-left diag- doesnt reach row 0
            i = total - 7
            j = 7
            while i < row:
                if board[i][j] == turn:
                    lst = lst + [[i,j]] 
                    i += 1
                    j -= 1
                else:
                    i += 1
                    j -= 1
            i = 7
            j = total - i
            while i > row:
                if board[i][j] == turn:
                    lst = lst + [[i,j]] 
                    i -= 1 
                    j += 1
                else:
                    i -= 1
                    j += 1            
        diff = row - col
        if diff > 0: #upper left diag&lower right- doesnt reach row 0
            i = diff
            j = 0
            while i < row:
                if board[i][j] == turn:
                    lst = lst + [[i,j]] 
                    i += 1
                    j += 1
                else:
                    i += 1
                    j += 1
            i = 7
            j = 7 - diff
            while i > row:
                if board[i][j] == turn:
                    lst = lst + [[i,j]] 
                    i -= 1
                    j -= 1
                else:
                    i -= 1
                    j -= 1
                
        if diff <= 0: #upper left diag&lower right- reaches row 0
            i = 0
            j = col - row
            while i < row:
                if board[i][j] == turn:
                    lst = lst + [[i,j]] 
                    i += 1
                    j += 1
                else:
                    i += 1
                    j += 1  
            i = 7 + diff
            j = 7
            while i > row:
                if board[i][j] == turn:
                    lst = lst + [[i,j]] 
                    i -= 1 
                    j -= 1
                else:
                    i -= 1
                    j -= 1  
        return lst   

def filter_lst(board, turn, row, col, lst, lon):
    '''
    Returns False if lst equals False, otherwise,
    returns a list of coordinates of disc of same colour turn which
    are the closest to position row, col in each direction on the board
    
    filter_lst: (listof (listof Str)) Str Nat Nat (listof (list Nat Nat)) Any -> (anyof Bool (listof (list Nat Nat)))
    Requires: as stated on the top, 0 <= row, col <= 7
    
    Examples:
       filter_lst(board1,'W',3,4,False,3) => False
       L = [[6, 1], [0, 5], [2, 5], [5, 5], [4, 7], [4, 3]]
       filter_lst(board1,'B',6,5,L,[]) => [[6, 1], [5, 5], [4, 7], [4, 3]]
    '''
    lon = []
    if lst == False:
        return False    
    if lst == []:
        return False
    else:
        for i in range(len(lst)):
            if lst[i][0] == row: #row
                lon = lon + [lst[i]]
        a = -1
        b = 0
        for i in range(len(lst)):
            if lst[i][1] == col: #closest col-up
                if lst[i][0] < row:
                    if lst[i][0] > a:
                        a = lst[i][0]
                        b = lst[i][1]
        if a != -1:
            lon = lon + [[a,b]] 
        a = 8
        for i in range(len(lst)):
            if lst[i][1] == col: #closest col-down               
                if lst[i][0] > row:
                    if lst[i][0] < a:
                        a = lst[i][0]
                        b = lst[i][1] 
        if a != 8:
            lon = lon + [[a,b]]        
        a = 8
        for i in range(len(lst)):                
            if lst[i][0] > row: #closest diag-down
                if lst[i][1] > col: #lower right
                    if lst[i][0] < a:
                        a = lst[i][0]
                        b = lst[i][1] 
        if a != 8:
            lon = lon + [[a,b]]                             
        a = 8
        for i in range(len(lst)):  
            if lst[i][0] > row:
                if lst[i][1] < col: #lower left
                    if lst[i][0] < a:
                        a = lst[i][0]
                        b = lst[i][1]  
        if a != 8:
            lon = lon + [[a,b]]  
        a = -1
        for i in range(len(lst)):      
            if lst[i][0] < row: #closest diag-up
                if lst[i][1] > col: #upper right
                    if lst[i][0] > a:
                        a = lst[i][0]
                        b = lst[i][1]  
        if a != -1:
            lon=lon+[[a,b]]              
        a = -1
        for i in range(len(lst)):      
            if lst[i][0] < row:     
                if lst[i][1] < col: #upper left
                    if lst[i][0] > a:
                        a = lst[i][0]
                        b = lst[i][1] 
        if a != -1:
            lon = lon + [[a,b]]    
    return lon  

def if_valid(board, turn, row, col, lon):
    '''
    Returns True if any position in lon is located at least one square away 
    (either horizontal, vertical or diagonal) from coordinate row, col and
    all the squares between the position and cooridnate row, col is not empty,
    returns False if lon equals False or the conditions above are not satisfied
    
    if_valid: (listof (listof Str)) Str Nat Nat (listof (list Nat Nat)) -> Bool
    Requires: as stated on the top, 0 <= row, col <= 7
    
    Examples: 
       if_valid(board1, 'B', 2, 7, False) => False
       if_valid(board1, 'W', 0, 7, [[0, 6], [5, 7]]) => False
       if_valid(board1, 'W', 5, 6, [[5, 1], [5, 7], [3, 6]]) => True
    '''
    if lon == False:
        return False
    for i in range(len(lon)): 
        if lon[i][0] == row: #row
            if lon[i][1] < col: #left
                y = lon[i][1]
                acc = 0
                if y != col - 1:
                    for j in range(y + 1,col):
                        if board[row][j] != '':
                            acc += 1
                    if acc == col - y - 1:
                        return True
            if lon[i][1] > col: #right
                y = lon[i][1]
                acc = 0
                if y != col + 1:
                    for j in range(col + 1,y):
                        if board[row][j] != '':
                            acc += 1
                    if acc == y - col - 1:
                        return True  
        if lon[i][1] == col: #col
            if lon[i][0] < row: #up
                x = lon[i][0]
                acc = 0
                if x != row - 1:
                    for j in range(x + 1,row):
                        if board[j][col] != '':
                            acc += 1
                    if acc == row - x - 1:
                        return True
            if lon[i][1] > row: #down
                x = lon[i][0]
                acc = 0
                if x != row + 1:
                    for j in range(row + 1,x):
                        if board[j][col] != '':
                            acc += 1
                    if acc == x - row - 1:
                        return True  
        if lon[i][0] < row: #upper-diag
            if lon[i][1] < col: #upper left
                x = lon[i][0]
                y = lon[i][1]
                acc = 0
                if x != row - 1:
                    for j in range(1,row - x):
                        if board[x + j][y + j] != '':
                            acc += 1
                    if acc == row - x - 1:
                        return True
            if lon[i][1] > col: #upper right
                x = lon[i][0]
                y = lon[i][1]
                acc = 0
                if x != row - 1:
                    for j in range(1,row - x):                    
                        if board[x + j][y - j] != '':
                            acc += 1
                    if acc == row - x - 1:
                        return True
        if lon[i][0] > row:
            if lon[i][1] > col: #lower right
                x = lon[i][0]
                y = lon[i][1]
                acc = 0
                if x != row + 1:
                    for j in range(1,x - row):
                        if board[x - j][y - j] != '':
                            acc += 1
                    if acc == x - row - 1:
                        return True
            if lon[i][1] < col: #lower left
                x = lon[i][0]
                y = lon[i][1]
                acc = 0
                if x != row + 1:
                    for j in range(1,x - row):
                        if board[x - j][y + j] != '':
                            acc += 1
                    if acc == x - row - 1:
                        return True 
    return False

def possible_pos(board, turn, row, col):
    '''
    Returns True if the disc of colour turn could be placed (valid)
    at position row, col on the board, False othewise.
    
    possible_pos: (listof (listof Str)) Str Nat Nat -> (listof (list Nat Nat))
    Requires: as stated on the top, 0 <= row, col <= 7
    
    Examples:
       possible_pos(board1,'B',2,3) => True
       possible_pos(board1,'B',5,6) => False
    '''
    a = same_loc(board, turn, row, col, [])
    b = filter_lst(board, turn, row, col, a, [])
    c = if_valid(board, turn, row, col, b)
    return c

def othello(board, turn, row, col):
    '''
    Returns True if the disc of colour turn could be placed (valid)
    at position row, col on the board, False othewise.
    
    othello: (listof (listof Str)) Str Nat Nat -> (listof (list Nat Nat))
    Requires: as stated on the top, 0 <= row, col <= 7
    
    Examples:
       othello(board1,'B',2,3) => True
       othello(board1,'B',5,6) => False
    '''    
    return possible_pos(board, turn, row, col)

## Examples:
check.expect("ex1",othello(board1,'B',2,3),True)
check.expect("ex2",othello(board1,'B',5,6),False)

## Tests:
check.expect("T1: corner-(0,0)",othello(board1,'B',0,0),True)
check.expect("T2: corner-(0,7)",othello(board1,'B',0,7),True)
check.expect("T3: corner-(7,0)",othello(board1,'B',7,0),False)
check.expect("T4: corner-(7,7)",othello(board1,'B',7,7),False)
check.expect("T5: col0",othello(board1,'B',5,0),True)
check.expect("T6: row0",othello(board1,'B',0,2),True)
check.expect("T7: col7",othello(board1,'B',6,7),True)
check.expect("T8: (2,3)",othello(board1,'B',2,3),True)
check.expect("T9: (1,6)",othello(board1,'B',1,6),True)
check.expect("T10: (6,2)",othello(board1,'B',6,2),True)
check.expect("T11: (5,6)",othello(board1,'B',5,6),False)
check.expect("T12: row7",othello(board1,'W',7,1),True)
check.expect("T13: (7,3)",othello(board1,'B',7,3),True)
