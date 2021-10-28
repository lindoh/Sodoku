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

#The digits to use to check the validity of the board
digits = '123456789'

#Check the validity of each row
def validate_rows (Board):
    for row in Board:
        for digit in digits:
            if row.find(digit) == -1:   #Check if you find all the digits from each row
                return False
            if row.count(digit) > 1:    #Check if a digit is counted more than once
                return False
    #If all is well then return true
    return True


#------------Sample Test------------------------------------------------------------------------
if validate_rows(Board1):
    print('Yes')
else:
    print('No')