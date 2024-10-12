from math import *
bc = '\033[30m'
wc = '\033[37m'

pawn = "♟"
knight = "♞"
bishop = "♝"
rook = "♜"
queen = "♛"
king = "♚"
a = [[bc+"♜"],[bc+"♞"],[bc+"♝"],[bc+"♛"],[bc+"♚"],[bc+"♝"],[bc+"♞"],[bc+"♜"]]
b = [[bc+pawn],[bc+pawn],[bc+pawn],[bc+pawn],[bc+pawn],[bc+pawn],[bc+pawn],[bc+pawn]]
c = [[],[],[],[],[],[],[],[]]
d = [[],[],[],[],[],[],[],[]]
e = [[],[],[],[],[],[],[],[]]
f = [[],[],[],[],[],[],[],[]]
g = [[wc+pawn],[wc+pawn],[wc+pawn],[wc+pawn],[wc+pawn],[wc+pawn],[wc+pawn],[wc+pawn]]
h = [[wc+"♜"],[wc+"♞"],[wc+"♝"],[wc+"♛"],[wc+"♚"],[wc+"♝"],[wc+"♞"],[wc+"♜"]]
board = [a,b,c,d,e,f,g,h]

def king_func(piece,sc) : 
    t_val = [] ; val = []
    if bc in piece : 
        color = bc 
    else : 
        color = wc
    for i in range(8) : 
        for j in range(8) : 
            try : 
                if (fabs(sc[0] - i) == 1.0) and (fabs(sc[1] - j) == 0.0) : 
                    t_val.append([i,j])
            except : 
                pass
            try : 
                if (fabs(sc[0] - i) == 0.0) and (fabs(sc[1] - j) == 1.0) : 
                    t_val.append([i,j])
            except : 
                pass
            try : 
                if (fabs(sc[0] - i) == 1.0) and (fabs(sc[1] - j) == 1.0) : 
                    t_val.append([i,j])
            except : 
                pass
    for i in t_val : 
        if board[i[1]][i[0]] != [] and color in board[i[1]][i[0]][0] :
            pass
        else : 
            val.append(i)
    return val

def rook_func(piece,sc) : 
    if bc in piece : 
        color = bc 
    else : 
        color = wc
    left = []
    right = []
    up = []
    down = []
    for i in range(8) : 
        for j in range(8) : 
            try : 
                if sc[0] == i : 
                    if sc[1] > j : 
                        up.append([i,j])
                    else : 
                        down.append([i,j])
                if sc[1] == j : 
                    if sc[0] > i : 
                        left.append([i,j])
                    else :
                        right.append([i,j])
            except : 
                pass
    path_st = [left[::-1],right,up[::-1],down]
    val = []
    for i in path_st : 
        for j in i : 
            if j == [sc[0],sc[1]] : 
                continue
            if board[j[1]][j[0]] != [] and color in board[j[1]][j[0]][0] : 
                break
            else : 
                val.append(j)
    return val
def bishop_func(piece,sc) : 
    if bc in piece : 
        color = bc
    else : 
        color = wc
    up_left = [] 
    up_right = []
    down_left = []
    down_right = []
    for i in range(8) : 
        for j in range(8) : 
            try : 
                if fabs(sc[0] - i) == fabs(sc[1]-j) :   
                    if sc[0] > i : 
                        if sc[1] < j : 
                            down_left.append([i,j])
                        else : 
                            up_left.append([i,j])
                    else : 
                        if sc[1] < j : 
                            down_right.append([i,j])
                        else : 
                            up_right.append([i,j])
            except : 
                pass
    path_diag = [up_left[::-1],up_right,down_left[::-1],down_right]
    val = []
    for i in path_diag :
        for j in i : 
            if j == [sc[0],sc[1]] : 
                continue
            if board[j[1]][j[0]] != [] and color in board[j[1]][j[0]][0] : 
                break
            else : 
                val.append(j)
    return val
def knight_func(piece,sc) : 
    t_val = []
    val = []
    if bc in piece :
        color = bc 
    else : 
        color = wc
    for i in range(8) : 
        for j in range(8) : 
            try : 
                if fabs(sc[1] - j) == 2.0 and fabs(sc[0] - i) == 1.0: 
                    t_val.append([i,j])
            except : 
                pass
            try : 
                if fabs(sc[1] - j) == 1.0 and fabs(sc[0]-i) == 2.0 : 
                    t_val.append([i,j])
            except : 
                pass
    for i in t_val : 
        if board[i[1]][i[0]] != [] and color in board[i[1]][i[0]][0] :
            pass
        else : 
            val.append(i)
    return val
def queen_func(piece,sc) : 
    if bc in piece : 
        color = bc 
    else : 
        color = wc
    up_left = [] 
    up_right = []
    down_left = []
    down_right = []
    left = []
    right = []
    up = []
    down = []
    for i in range(8) : 
        for j in range(8) : 
            try : 
                if fabs(sc[0] - i) == fabs(sc[1]-j) :   
                    if sc[0] > i : 
                        if sc[1] < j : 
                            down_left.append([i,j])
                        else : 
                            up_left.append([i,j])
                    else : 
                        if sc[1] < j : 
                            down_right.append([i,j])
                        else : 
                            up_right.append([i,j])
            except :    
                pass    
            try : 
                if sc[0] == i : 
                    if sc[1] > j : 
                        up.append([i,j])
                    else : 
                        down.append([i,j])
                if sc[1] == j : 
                    if sc[0] > i : 
                        left.append([i,j])
                    else :
                        right.append([i,j])
            except : 
                pass
    path_diag = [up_left[::-1],up_right,down_left[::-1],down_right]
    path_st = [left[::-1],right,up[::-1],down]
    val = []
    for i in path_diag :
        for j in i : 
            if j == [sc[0],sc[1]] : 
                continue
            if board[j[1]][j[0]] != [] and color in board[j[1]][j[0]][0] : 
                break
            else : 
                val.append(j)
    for i in path_st : 
        for j in i : 
            if j == [sc[0],sc[1]] : 
                continue
            if board[j[1]][j[0]] != [] and color in board[j[1]][j[0]][0] : 
                break
            else : 
                val.append(j)
    return val
def print_board() : 
    print("    A    B    C    D    E    F    G    H"+"\n-------------------------------------------")
    for i in range(len(board)) : 
        print(f"{i+1} | ",end="")
        for j in board[i] :
            if len(j) == 1 :
                print(j[0],end=wc+"  | "+wc)
            else : 
                print(" ",end=wc+"  | "+wc)
        print()
    print("-------------------------------------------")
print_board()
def move() : 
    startpos = input("Enter the starting position of ur piece : ")
    endpos = input("Enter the ending position of ur piece : ")
    piece = board[int(startpos[1])-1][ord(startpos[0])-97]
    validation = valid_move(piece,startpos,endpos)
    if validation[0] : 
        board[int(startpos[1])-1][ord(startpos[0])-97] = []
        board[int(endpos[1])-1][ord(endpos[0])-97] = [validation[1]]
        print_board()
    else :
        print("invalid move")
def pos_point(pos) :
    x = ord(pos[0])-97 
    y = int(pos[1])-1
    return [x,y]
def point_pos(pos) : 
    m1=chr(pos[0]+97)
    m2=str(pos[1]+1)
    return m1+m2
def valid_move(piece,startpos,endpos) : 
    sc = pos_point(startpos)
    ec = pos_point(endpos)
    piece = piece[0]
    if pawn in piece : 
        if wc in piece : 
            if not(board[ec[1]][ec[0]] != [] and wc in board[ec[1]][ec[0]][0]) : 
                doubmove = ["a7","b7","c7","d7","e7","f7","g7","h7"]
                promote = ["a1","b1","c1","d1","e1","f1","g1","h1"]
                if startpos in doubmove : 
                    spm = 2
                    doubmove.remove(startpos)
                else : 
                    spm=1
                if sc[0] != ec[0] and (sc[1]-ec[1] == 1) : 
                        try :
                            if board[sc[1]-1][sc[0]+1] != []: 
                                if endpos == point_pos([sc[0]+1,sc[1]-1]) : 
                                    R = True
                                else : 
                                    R =  False
                        except : 
                            pass
                        try : 
                            if board[sc[1]-1][sc[0]-1] != [] :   
                                if endpos == point_pos([sc[0]-1,sc[1]-1]) : 
                                    R =  True 
                                else :  
                                    R =  False
                        except :
                            pass
                elif ((sc[1] - ec[1] == 1)or(sc[1]-ec[1] == spm)) and (sc[0] == ec[0]) : 
                    R = True
                else :
                    R = False
                if R :
                    if endpos in promote : 
                        pro = input("Enter what u want the pawn to become (Q,K,R,B) : ").upper()
                        if pro == "Q" :
                            piece = wc+"♛"
                        elif pro == "R" : 
                            piece = wc+"♜"
                        elif pro == "K" : 
                            piece = wc+"♞"
                        elif pro == "B" : 
                            piece = wc+"♝"
                        else : 
                            print("err")
            else : 
                R = False
        if bc in piece : 
            if not(board[ec[1]][ec[0]] != [] and bc in board[ec[1]][ec[0]][0]) :
                doubmove = ["a2","b2","c2","d2","e2","f2","g2","h2"]
                promote = ["a8","b8","c8","d8","e8","f8","g8","h8"]
                if startpos in doubmove : 
                    spm = 2
                    doubmove.remove(startpos)
                else : 
                    spm=1
                if sc[0] != ec[0] and (ec[1] - sc[1] == spm) : 
                    try : 
                        if board[sc[1]+1][sc[0]+1] != []: 
                            if endpos == point_pos([sc[0]+1,sc[1]+1]) : 
                                R = True
                            else : 
                                R = False
                    except : 
                        pass
                    try : 
                        if board[sc[1]+1][sc[0]-1] != [] :   
                            if endpos == point_pos([sc[0]-1,sc[1]+1]) : 
                                R = True 
                            else :  
                                R = False
                    except : 
                        pass
                elif ((ec[1] - sc[1] == 1) or ec[1]-sc[1] == spm) and (sc[0] == ec[0]) : 
                    R = True
                else :
                    R = False
                if R :
                    if endpos in promote : 
                        pro = input("Enter what u want the pawn to become (Q,K,R,B) : ").upper()
                        if pro == "Q" :
                            piece = bc+"♛"
                        elif pro == "R" : 
                            piece = bc+"♜"
                        elif pro == "K" : 
                            piece = bc+"♞"
                        elif pro == "B" : 
                            piece = bc+"♝"
                        else : 
                            print("err")
            else : 
                R = False
    elif knight in piece : 
        R = False
        if ec in knight_func(piece,sc) : 
            R = True
    elif bishop in piece :
        R = False
        if ec in bishop_func(piece,sc) : 
            R = True
    elif rook in piece : 
        R = False
        if ec in rook_func(piece,sc) : 
            R = True
    elif queen in piece : 
        R = False
        if ec in queen_func(piece,sc) : 
            R = True
    elif king in piece : 
        R = False  
        if ec in king_func(piece,sc) : 
            R = True
    else :
        print("hehe")
        R = True ; piece=piece
    return [R,piece]

def see_king(piece,pos) : 
    piece = piece[0]
    sc = pos_point(pos)
while True : 
    move()
    
