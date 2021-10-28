#Create the Sodoku board(s)
Board1 = ['295743861',
          '431865927',
          '876192543',
          '387459216',
          '612387495',
          '549216738',
          '763524189',
          '928671354',
          '154938672']

Board2 = ['195743862',
          '431865927',
          '876192543',
          '387459216',
          '612387495',
          '549216738',
          '763524189',
          '928671354',
          '254938671']

#--------------Check the validity of each row---------------
def validate_row(Board):
    for row in Board:
        for digit in range(1, 10):
            if row.find(str(digit)) == -1:   #Check if you find all the digits from each row
                return False
            if row.count(str(digit)) > 1:    #Check if a digit is counted more than once
                return False
    #If all is well then return true
    return True

#--------------Check the validity of each column---------------
def validate_column(Board):
    digits = ''
    column = []

    #Create a Board of columns in a horizontal form for ease of use
    for i in range(9):
        for row in Board: 
            digits += row[i]
        column.append(digits)
        digits = ''

    #The validate_row function can be used to check each column
    valid = validate_row(column)
    return valid

#--------------Check the validity of each 3X3 sub-square---------------
def validate_sub_sqr(Board):
    new_board = [[elem for elem in row] for row in Board]
    mask = ''
    r_start = c_start = 0
    r_end = c_end = 3

    while r_end < 10:
        for i in range(r_start, r_end):
            for j in range(c_start, c_end):
                mask += new_board[i][j]
        
        for digit in range(1, 10):
            if mask.find(str(digit)) == -1:
                return False
            if mask.count(str(digit)) > 1:
                return False
        mask = ''
        c_start += 3
        c_end += 3
        if c_end > 10:
            r_start += 3
            r_end += 3
            c_start = 0
            c_end = 3

    #If all is well return True
    return True


#------------Sample Test------------------------------------------------------------------------
if validate_row(Board2) and validate_column(Board2) and validate_sub_sqr(Board2):
    print('Yes')
else:
    print('No')


