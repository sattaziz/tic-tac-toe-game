row_1 = ['-', '    |    ', '-', '    |    ', '-']
row_2 = ['-', '    |    ', '-', '    |    ', '-']
row_3 = ['-', '    |    ', '-', '    |    ', '-']

l = [row_1, row_2, row_3]

change_status = True
count = 1


def check_for_valid_inputs(s):
    if s not in range(0, 5):
        return False
    else:
        return True


def greeting():
    return "Hello, it's tic-tac-toe game!"


print(greeting())


while change_status:
    if count % 2 == 0:
        print("0's move")
    else:
        print("X's move")
    row = int(input("Enter the row: ")) - 1
    column = int(input("enter the column: "))
    column_index = 0
    if column == 1:
        column_index = 0
    elif column == 2:
        column_index = 2
    else:
        column_index = 4

    if check_for_valid_inputs(row):
        if count % 2 == 0:
            l[row][column_index] = '0'
        else:
            l[row][column_index] = 'X'
        print(row_1[0] + row_1[1] + row_1[2] + row_1[3] + row_1[4])
        print(row_2[0] + row_2[1] + row_2[2] + row_2[3] + row_2[4])
        print(row_3[0] + row_3[1] + row_3[2] + row_3[3] + row_3[4])
    else:
        print("Input is incorrect!")

    if row_1[0] == 'X' and row_1[2] == 'X' and row_1[-1] == 'X':
        print("X wins!")
        change_status = False
    elif row_2[0] == 'X' and row_2[2] == 'X' and row_2[-1] == 'X':
        print("X wins!")
        change_status = False
    elif row_3[0] == 'X' and row_3[2] == 'X' and row_3[-1] == 'X':
        print("X wins!")
        change_status = False
    elif row_1[0] == 'X' and row_2[0] == 'X' and row_3[0] == 'X':
        print("X wins!")
        change_status = False
    elif row_1[2] == 'X' and row_2[2] == 'X' and row_3[2] == 'X':
        print("X wins!")
        change_status = False
    elif row_1[-1] == 'X' and row_2[-1] == 'X' and row_3[-1] == 'X':
        print("X wins!")
        change_status = False
    elif row_1[0] == 'X' and row_2[2] == 'X' and row_3[-1] == 'X':
        print("X wins!")
        change_status = False
    elif row_1[-1] == 'X' and row_2[2] == 'X' and row_3[0] == 'X':
        print("X wins!")
        change_status = False

    if row_1[0] == '0' and row_1[2] == '0' and row_1[-1] == '0':
        print("0 wins!")
        change_status = False
    elif row_2[0] == '0' and row_2[2] == '0' and row_2[-1] == '0':
        print("0 wins!")
        change_status = False
    elif row_3[0] == '0' and row_3[2] == '0' and row_3[-1] == '0':
        print("0 wins!")
        change_status = False
    elif row_1[0] == '0' and row_2[0] == '0' and row_3[0] == '0':
        print("0 wins!")
        change_status = False
    elif row_1[2] == '0' and row_2[2] == '0' and row_3[2] == '0':
        print("0 wins!")
        change_status = False
    elif row_1[-1] == '0' and row_2[-1] == '0' and row_3[-1] == '0':
        print("0 wins!")
        change_status = False
    elif row_1[0] == '0' and row_2[2] == '0' and row_3[-1] == '0':
        print("0 wins!")
        change_status = False
    elif row_1[-1] == '0' and row_2[2] == '0' and row_3[0] == '0':
        print("0 wins!")
        change_status = False

    count += 1
