a1 = [2, 4, 3, 1]
a2 = [1, 3, 4, 2]
a3 = [3, 1, 2, 4]
a4 = [4, 2, 1, 3]

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
        # print("Curr Queen Row = ", curr_queen_row)   TESTING
        # print("Curr Queen Col = ", curr_queen_col)   TESTING
        next_queen = Q_positions[index]
        next_queen_row = next_queen[0]
        next_queen_col = next_queen[1]
        # print("Next Queen Row = ", next_queen_row)   TESTING
        # print("Next Queen Col = ", next_queen_col)   TESTING
        while curr_queen_row >= 0 and curr_queen_col <= 4:
            curr_queen_row = curr_queen_row-1
            curr_queen_col = curr_queen_col+1
            if curr_queen_row == next_queen_row and curr_queen_col == next_queen_col:
                # print(curr_queen_row,curr_queen_col)  TESTING
                # print(next_queen_row,next_queen_col)  TESTING
                attacks = attacks+1
    return attacks

# def Up_Right_Attacks(Curr_Q,Next_Q):
#     curr_queen_row=Curr_Q[0]
#     curr_queen_col=Curr_Q[1]
#     next_queen_row = Next_Q[0]
#     next_queen_col = Next_Q[1]
#     attacks=0
#     while curr_queen_row >= 0 and curr_queen_col <= 4:
#         curr_queen_row = curr_queen_row-1
#         curr_queen_col = curr_queen_col+1
#         if curr_queen_row == next_queen_row and curr_queen_col == next_queen_col:
#             attacks = attacks+1
#     return attacks

# for index in range(4):
#     print("Outer Loop = ",  index)
#     for i in range(index+1,4):
#         print("Inner Loop = ",  i)

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
    count = 0
    # getting the positios of all the queens
    Q_positions = All_Queen_Positions(a1)
    for index in range(len(a1)):
        Curr_Q = Queen_possitions(index, a1)
        for i in range(0, index+1):
            # Next_Q = Queen_possitions(i, a1)
            # up_right_attacks=Up_Right_Attacks(Curr_Q,Next_Q)
            # checking upper_right diagonal
            up_right = Upper_Right(Curr_Q, Q_positions, index+1)


# arr=All_Queen_Positions(a1)
# print(arr)

# Count_row=Row_Attacks(a1);
# print(Count_row)
# Q_positions = All_Queen_Positions(a1)
# Curr_Q=[3,1]
# up_right = Upper_Right(Curr_Q, Q_positions, 2)

# print(up_right)