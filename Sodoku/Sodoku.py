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

#Check the validity of each row
def validate_rows (Board):
    for row in Board:
        for digit in range(1, 10):
            if row.find(str(digit)) == -1:   #Check if you find all the digits from each row
                return False
            if row.count(str(digit)) > 1:    #Check if a digit is counted more than once
                return False
    #If all is well then return true
    return True

#Check the validity of each column
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
    valid = validate_rows(column)
    return valid





#------------Sample Test------------------------------------------------------------------------
if validate_rows(Board2) and validate_column(Board2):
    print('Yes')
else:
    print('No')

