sudoku_list = [[0, 0, 6, 1, 0, 0, 0, 0, 0], [0, 8, 0, 0, 9, 0, 0, 3, 0], [2, 0, 0, 0, 0, 0, 4, 0, 0], [4, 0, 0, 0, 0, 1, 8, 0, 0], [0, 3, 0, 0, 7, 0, 0, 4, 0], [0, 0, 7, 9, 0, 0, 0, 0, 3], [0, 0, 8, 4, 0, 0, 0, 0, 6], [0, 2, 0, 0, 5, 0, 0, 8, 0], [1, 0, 0, 0, 0, 2, 5, 0, 0]]

def displayListBox(sudoku_list):
    rowColumnNum = len(sudoku_list)
    print('-'*(2*rowColumnNum) + '-----')
    for column in range(rowColumnNum):
        column_num = column + 1
        row_num = 0
        for row in range(rowColumnNum): 
            
            if row_num%3 == 0 and row_num != 0:
                print('| ',end='')
            print('|'+str(sudoku_list[column][row]),end='' )
            row_num +=1
        print('|')
        
        if column_num %3 == 0:
            print('-'*(2*rowColumnNum) + '-----')


def is_it_right_place(x,y,num):
    global sudoku_list
    # row control
    for i in range(9):
        if sudoku_list[y][i] == num:
            return False
    #column control
    for j in range(9):
        if sudoku_list[j][x] == num:
            return False
    
    #square control
    x_square = (x // 3)*3
    y_square = (y // 3)*3
    for i in range(x_square ,x_square+3):
        for j in range(y_square,y_square+3):
            if sudoku_list[j][i] == num:
                return False
    
    return True
def solving_sudoku():
    global sudoku_list
    for column in range(9):
        for row in range(9):
            if sudoku_list[column][row] == 0:
                for number in range(1,10):
                    if is_it_right_place(row,column,number):
                        sudoku_list[column][row]= number
                        solving_sudoku()
                        sudoku_list[column][row] = 0
                return sudoku_list
    
    displayListBox(sudoku_list)

solving_sudoku()
