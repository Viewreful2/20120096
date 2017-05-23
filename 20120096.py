def rule1(B) :
    for i in range(0,5) :
        if (B[i][0] +B[i][1] +B[i][2] +B[i][3] +B[i][4]) == 5:
            return True;
    return False;

def rule2(B):
    for i in range(0,5) :
        if (B[0][i] +B[1][i] +B[2][i] +B[3][i] +B[4][i]) == 5:
            return True;
    return False;

def rule3(B):
    count = 0
    for i in range(0,5) :
        if B[i][i] == 1:
            count = count +1
    if count == 5 :
        return True;

    count = 0
    for i in range(0,5):
        if B[i][4-i] == 1:
            count = count +1
    if count == 5 :
        return True;
    
    return False;


def rule4(B):
    if (B[0][0] +B[0][4] +B[4][0] +B[4][4]) == 4:
        return True;
    
    return False;    



row = 5
col = 5

BINGO = []
B = []
T = int(input())

for t in range(0,T):
    BINGO = []
    B = []
    for i in range(0, row):
        row_input = input().split()
        row_input = [int(j) for j in row_input]
        BINGO.append(row_input)
        
        if i == 2 :
            B.append([0,0,1,0,0])
        else :
            B.append([0]*5)
            
    input_numbers = input().split()
    input_numbers = [int(j) for j in input_numbers]

    count_of_input = 0
    for number in input_numbers:

        count_of_input = count_of_input + 1

        for i in range(0,5):
            for j in range(0,5):
                if number == BINGO[i][j]:
                    B[i][j] = 1
                    
        if rule1(B) == True:
            print(count_of_input)
            break

        if rule2(B) == True:
            print(count_of_input)
            break


        if rule3(B) == True:
            print(count_of_input)
            break

        if rule4(B) == True:
            print(count_of_input)
            break