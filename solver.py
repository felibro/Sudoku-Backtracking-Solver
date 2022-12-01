import numpy as np

def checker(board):
    pass

def pretty_print(board):
    for i in range(len(board)):
        print(board[i])

def box(coor): #in 0-8 coor col row
    return ((coor[0])//3*3, (coor[1])//3*3)

def box_nums(coor, board): #takes in BOX coor (3,3), (6,6),etc, returns already filled/clues
    listy = []
    a = board[coor[0]:coor[0]+3, coor[1]:coor[1]+3].flatten()
    return a[a!=0] #works i think

def row_nums(coor, board):
    r = board[coor[0]]
    return r[r!=0]

def col_nums(coor, board):
    c = board[:,coor[1]]
    return c[c!=0]
    

def check(coor, board, n): #returns available
    c = box(coor)
    if n in box_nums(c, board) or n in board[:,coor[1]] or n in board[coor[0]]:
        return False
    return True
    
def my_func(coor, board): #start at (0,0)
    global nums
    if coor[0]==9:
        return True
    if coor[1]==9:
        return my_func((coor[0]+1, 0), board) #start new line
    if board[coor[0], coor[1]] != 0: 
        return my_func((coor[0], coor[1]+1), board) #skip over
        #get availavle list
        #if lsit is empty, backtrack
        
    for num in nums:
        if check((coor[0], coor[1]), board, num):
            board[coor[0], coor[1]] = num
            #print(board)
            
            if my_func((coor[0], coor[1]+1), board):
                return True
    board[coor[0], coor[1]] = 0
    return False    
        
    
def generator(board):
    b = my_func((0,0), board)
    print(board)
    
if __name__=='__main__':
    nums = [i for i in range(1,10)]
    
    with open("board.txt", "r") as f:
        b = f.read()

    board = np.array(list(str(b.split()[0]))).reshape(9,9).astype(int)
    generator(board)
