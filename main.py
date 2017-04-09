import random
import numpy as np

global signal
def initTable(list, num):
    for i in xrange(0, 10, 1):
        for j in xrange(0, 10, 1):
            list[i][j] = random.randint(1, num)
    pass

def checkTable(table):
    same = 0
    for i in xrange(0, 10, 1):
        for j in xrange(0, 8, 1):
            if table[i][j] == table[i][j + 1] and table[i][j + 1] == table[i][j + 2]:
                same += 1
    for i in xrange(0, 10, 1):
        for j in xrange(0, 8, 1):
            if table[j][i] == table[j + 1][i] and table[j + 1][i] == table[j + 2][i]:
                same += 1
    if same >= 1:
        return True
    else:
        return False

def printTable(table,num):
    if checkTable(table) == True:
        print("table refresh")
        initTable(table, num)
        printTable(table, num)
    else:
        print(table)


def checkCoor(x1, y1, x2, y2):
    status = 0
    if x1 == x2 and y1 == y2:
        status = 1
        return status
    elif x1 != x2 and y1 == y2:
        if x1 + 1 != x2 and x1 - 1 != x2:
            status = 2
            return status
        else:
            status = 3
            return status
    elif x1 == x2 and y1 != y2:
        if y1 + 1 != y2 and y1 - 1 != y2:
            status = 4
            return status
        else:
            status = 5
            return status
    else:
        status = 6
        return status


def swapx(table, x1, x2, y, num):
    global signal
    i = 10 - y
    j1 = x1 - 1
    j2 = x2 - 1
    temp = table[i][j1]
    table[i][j1] = table[i][j2]
    table[i][j2] = temp
    if (checkTable(table)):
        print("nice")
        searchConnected(table)
        print(drop(table, signal, num))
    else:
        print("change failed")
        temp = table[i][j1]
        table[i][j1] = table[i][j2]
        table[i][j2] = temp
        print(table)


def swapy(table, x, y1, y2, num):
    global signal
    i1 = 10 - y1
    i2 = 10 - y2
    j = x - 1
    temp = table[i1][j]
    table[i1][j] = table[i2][j]
    table[i2][j] = temp
    if (checkTable(table)):
        print("nice")
        searchConnected(table)
        print(drop(table, signal, num))
    else:
        print("change failed")
        temp = table[i1][j]
        table[i1][j] = table[i2][j]
        table[i2][j] = temp
        print(table)



def threesame(table, a1, b1, a2, b2, a3, b3):
    table[a1][b1] = 0
    table[a2][b2] = 0
    table[a3][b3] = 0


def foursame(table, a1, b1, a2, b2, a3, b3, a4, b4):
    table[a1][b1] = 0
    table[a2][b2] = 0
    table[a3][b3] = 0
    table[a4][b4] = 0


def fivesame(table, a1, b1, a2, b2, a3, b3, a4, b4, a5, b5):
    table[a1][b1] = 0
    table[a2][b2] = 0
    table[a3][b3] = 0
    table[a4][b4] = 0
    table[a5][b5] = 0


def searchConnected(table):
    global signal
    for i in xrange(0, 10, 1):
        for j in xrange(0, 6, 1):
            if table[i][j] == table[i][j + 1] and table[i][j + 1] == table[i][j + 2] and table[i][j + 2] == table[i][
                        j + 3] and table[i][j + 3] == table[i][j + 4]:
                fivesame(table, i, j, i, j + 1, i, j + 2, i, j + 3, i, j + 4)
                signal = 5

    for i in xrange(0, 10, 1):
        for j in xrange(0, 7, 1):
            if table[i][j] == table[i][j + 1] and table[i][j + 1] == table[i][j + 2] and table[i][j + 2] == table[i][
                        j + 3]:
                foursame(table, i, j, i, j + 1, i, j + 2, i, j + 3)
                signal = 4

    for i in xrange(0, 10, 1):
        for j in xrange(0, 8, 1):
            if table[i][j] == table[i][j + 1] and table[i][j + 1] == table[i][j + 2]:
                threesame(table, i, j, i, j + 1, i, j + 2)
                signal = 3

    for i in xrange(0, 10, 1):
        for j in xrange(0, 6, 1):
            if table[j][i] == table[j + 1][i] and table[j + 1][i] == table[j + 2][i] and table[j + 3][i] == \
                    table[j + 2][i] and table[j + 3][i] == table[j + 4][i]:
                fivesame(table, j, i, j + 1, i, j + 2, i, j + 3, i, j + 4, i)
                signal = 5

    for i in xrange(0, 10, 1):
        for j in xrange(0, 7, 1):
            if table[j][i] == table[j + 1][i] and table[j + 1][i] == table[j + 2][i] and table[j + 2][i] == \
                    table[j + 3][i]:
                foursame(table, j, i, j + 1, i, j + 2, i, j + 3, i)
                signal = 4

    for i in xrange(0, 10, 1):
        for j in xrange(0, 8, 1):
            if table[j][i] == table[j + 1][i] and table[j + 1][i] == table[j + 2][i]:
                threesame(table, j, i, j + 1, i, j + 2, i)
                signal = 3


def drop(table, signal, num):
    for i in xrange(0, 10, 1):
        for j in xrange(0, 9, 1):
            if table[i][j] == 0 and table[i][j + 1] != 0:
                # vertical drop
                for k in xrange(0, signal + i, 1):
                    table[k + signal][j] = table[k][j]
                for l in xrange(0, signal, 1):
                    table[l][j] = random.randint(1, num)

            elif table[i][j] == 0 and table[i][j + 1] == 0:
                # horizontal drop
                if i == 0:
                    for k in xrange(j, j + signal, 1):
                        table[i][k] = random.randint(1, num)
                else:
                    for k in xrange(i, 0, -1):
                        for l in xrange(j, j + signal, 1):
                            table[k][l] = table[k - 1][l]
                    for x in xrange(j, j + signal, 1):
                        table[0][x] = random.randint(1, num)
    return table

def main():
    # To avoid stack overflow,input will be bigger than 4.
    table = np.zeros((10, 10), int)
    num = input("How many colors do you want?")
    initTable(table, num)
    printTable(table, num)

    while True:
        coor = raw_input("format:x1 y1 x2 y2,split with space :")
        if coor == "end":
            break
        else:
            coor_list = coor.split(' ', 5)
            x1 = int(coor_list[0])
            y1 = int(coor_list[1])
            x2 = int(coor_list[2])
            y2 = int(coor_list[3])
            if checkCoor(x1, y1, x2, y2) == 1:
                print("same coordinate")
            elif checkCoor(x1, y1, x2, y2) == 6:
                print("error coordinate")
            elif checkCoor(x1, y1, x2, y2) == 2:
                print("error coordinate on x")
            elif checkCoor(x1, y1, x2, y2) == 4:
                print("error coordinate on y")
            elif checkCoor(x1, y1, x2, y2) == 3:
                print(swapx(table, x1, x2, y1, num))
            else:
                print(swapy(table, x1, y1, y2, num))
if __name__ == '__main__':
    main()



