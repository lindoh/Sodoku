
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
    #Convert the Board to a list of 9 3x3 lists (sub-squares)
    new_board = [[elem for elem in row] for row in Board] 
    mask = ''                   #A single 3x3 sub-square (list) 
    r_index = c_index = 0       #To control the start and end of the Board iteration

    #Create a mask and validate the digits in the mask
    while r_index < 7:
        for i in range(r_index, r_index + 3):
            for j in range(c_index, c_index + 3):
                mask += new_board[i][j]
        
        #Check if you find all the digits from each mask and if the count of each is > 1
        for digit in range(1, 10):
            if mask.find(str(digit)) == -1:
                return False
            if mask.count(str(digit)) > 1:
                return False

        mask = ''               #Clear mask before you create a new one
        c_index += 3            #Move the mask to the right by 3 columns
        if c_index > 7:
            r_index += 3        #Move the mask down by 3 rows
            c_index = 0         #Move the mask back to the starting point(left)

    #If all is well return True
    return True


#------------Sample Test------------------------------------------------------------------------
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

#Check if It's a valid Sodoku combination
if validate_row(Board1) and validate_column(Board1) and validate_sub_sqr(Board1):
    print('Yes')
else:
    print('No')


