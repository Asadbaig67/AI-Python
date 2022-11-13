a1 = [2, 4, 3, 1, 5]


# Function that returns the position coordinates of a single Queen
def Queen_possitions(index, a1):
    value = a1[index]
    return [value-1, index]

# Function that returns the position coordinates of a all Queens


def All_Queen_Positions(list):
    Q_array = []
    for index in range(len(list)):
        curr = Queen_possitions(index, list)
        Q_array.append(curr)
    return Q_array


def Upper_Right(Curr_Q, Q_positions, i):
    attacks = 0
    for index in range(i, len(Q_positions)):
        curr_queen_row = Curr_Q[0]
        curr_queen_col = Curr_Q[1]
        
        next_queen = Q_positions[index]
        next_queen_row = next_queen[0]
        next_queen_col = next_queen[1]
        
        while curr_queen_row >= 0 and curr_queen_col <= 4:
            curr_queen_row = curr_queen_row-1
            curr_queen_col = curr_queen_col+1
            if curr_queen_row == next_queen_row and curr_queen_col == next_queen_col:
                
                attacks = attacks+1
    return attacks


def Upper_Left(Curr_Q, Q_positions, i):
    attacks = 0
    for index in range(i, len(Q_positions)):
        curr_queen_row = Curr_Q[0]
        curr_queen_col = Curr_Q[1]
        
        next_queen = Q_positions[index]
        next_queen_row = next_queen[0]
        next_queen_col = next_queen[1]
        
        while curr_queen_row >= 0 and curr_queen_col <= 4:
            curr_queen_row = curr_queen_row-1
            curr_queen_col = curr_queen_col-1
            if curr_queen_row == next_queen_row and curr_queen_col == next_queen_col:
                
                attacks = attacks+1
    return attacks


def Bottom_Left(Curr_Q, Q_positions, i):
    attacks = 0
    for index in range(i, len(Q_positions)):
        curr_queen_row = Curr_Q[0]
        curr_queen_col = Curr_Q[1]
        
        next_queen = Q_positions[index]
        next_queen_row = next_queen[0]
        next_queen_col = next_queen[1]
        
        while curr_queen_row >= 0 and curr_queen_col <= 4:
            curr_queen_row = curr_queen_row+1
            curr_queen_col = curr_queen_col-1
            if curr_queen_row == next_queen_row and curr_queen_col == next_queen_col:
                
                attacks = attacks+1
    return attacks


def Bottom_Right(Curr_Q, Q_positions, i):
    attacks = 0
    for index in range(i, len(Q_positions)):
        curr_queen_row = Curr_Q[0]
        curr_queen_col = Curr_Q[1]
        
        next_queen = Q_positions[index]
        next_queen_row = next_queen[0]
        next_queen_col = next_queen[1]
        
        while curr_queen_row >= 0 and curr_queen_col <= 4:
            curr_queen_row = curr_queen_row+1
            curr_queen_col = curr_queen_col+1
            if curr_queen_row == next_queen_row and curr_queen_col == next_queen_col:
            
                attacks = attacks+1
    return attacks

# Checking for attacks in row


def Row_Attacks(a1):
    count = 0
    for index in range(len(a1)):
        curr = Queen_possitions(index, a1)
        for i in range(index+1, len(a1)):
            a = Queen_possitions(i, a1)
            if curr[0] == a[0]:
                count = count+1
    return count

# Diagonal attacks check


def Diagonal_Attacks(a1):
    
    Q_positions = All_Queen_Positions(a1)
    for index in range(len(a1)):
        Curr_Q = Queen_possitions(index, a1)
        up_right = Upper_Right(Curr_Q, Q_positions, index+1)
        up_left = Upper_Left(Curr_Q, Q_positions, index+1)
        bottom_right = Bottom_Right(Curr_Q, Q_positions, index+1)
        bottom_left = Bottom_Left(Curr_Q, Q_positions, index+1)
        total_attack_diagonal = up_left+up_right+bottom_left+bottom_right

    return total_attack_diagonal


a = Row_Attacks(a1)
b = Diagonal_Attacks(a1)

total_attack = a+b

print(total_attack)


