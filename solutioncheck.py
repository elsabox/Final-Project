# Code written by: Elizabeth Marella
# Andrew ID: emarella
# Last Updated: Nov 25, 2017

def solCheck(puzzle,mode=0):
    # takes a nested list with ten elements where each element, excluding the first element, is a list of
    # 9 lists where the elements of each list is a list containing the displayed digit, a correct solution,
    # and a word to determine whether or not the element can take user input or not

    
    # go through each digit
    for x in range(9):

        values = []
        
        # go through each row
        for i in range(9):

            for j in range(9):

                if puzzle[i+1][j+1][mode] != "":

                    values.append(int(puzzle[i+1][j+1][mode]))

            if x+1 not in values:

                return False

            values = []
        
        # go through each column
        for i in range(9):

            for j in range(9):

                if puzzle[j+1][i+1][mode] != "":

                    values.append(int(puzzle[j+1][i+1][mode]))
            
            if x+1 not in values:
            
                return False

            values = []
        
        # go through each sub-grid

        for k in range(0,9,3):
            
            for l in range(0,9,3):
                
                for i in range(3):

                    for j in range(3):

                        if puzzle[i+1+k][j+1+l][mode] != "":

                            values.append(int(puzzle[i+1+k][j+1+l][mode]))

                if x+1 not in values:

                    return False

                values = []


    return True


        
                    
