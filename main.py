# coding=utf-8
import random
import numpy as np

global signal
score = 0

def initTable(list, num):
    for i in xrange(0, 10, 1):
        for j in xrange(0, 10, 1):
            list[i][j] = random.randint(1, num)


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
        print("有連線，重新刷新盤面")
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
        print("交換成功")
        searchConnected(table)
        score_count(table)
        print(drop(table, signal, num))
    else:
        print("交換失敗")
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
        print("交換成功")
        searchConnected(table)
        score_count(table)
        print(drop(table, signal, num))
            
    else :
        print("交換失敗")
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
            if table[i][j] == 0 and table[i][j + 1] == 0:
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

    for i in xrange(9, -1, -1):
        for j in xrange(9, 0, -1):
            if table[i][j] == 0 and table[i][j - 1] != 0:
                # vertical drop
                for k in xrange(i, signal-1, -1):
                    table[k][j] = table[k-signal][j]
                for l in xrange(0, signal, 1):
                    table[l][j] = random.randint(1, num)
    for i in xrange(0,9,1):
        if table[i][0] == 0 and table[i+1][0] == 0:
            for k in xrange(i+signal-1, signal-1, -1):
                table[k][9] = table[k-signal][9]
            for l in xrange(0, signal, 1):
                table[l][9] = random.randint(1, num)
            
    return table

def score_count(table):
    global score
    for x in xrange(0,10):
        for y in xrange(0,10):
            if table[x][y] == 0:
                score += 1

def main():
    # To avoid stack overflow,input will be bigger than 4.
    table = np.zeros((10, 10), int)
    num = input("要產生幾種顏色?")
    initTable(table, num)
    printTable(table, num)
    while True:
        coor = raw_input("輸入要交換的座標，格式x1 y1 x2 y2 中間以空白分開，輸入end結束輸入")
        if coor == "end":
            break
        else:
            coor_list = coor.split(' ', 5)
            x1 = int(coor_list[0])
            y1 = int(coor_list[1])
            x2 = int(coor_list[2])
            y2 = int(coor_list[3])
            if checkCoor(x1, y1, x2, y2) == 1:
                print("你輸入了相同座標")
            elif checkCoor(x1, y1, x2, y2) == 6:
                print("輸入座標錯誤")
            elif checkCoor(x1, y1, x2, y2) == 2:
                print("x軸座標有誤")
            elif checkCoor(x1, y1, x2, y2) == 4:
                print("y軸座標有誤")
            elif checkCoor(x1, y1, x2, y2) == 3:
                swapx(table, x1, x2, y1, num)
                print("分數:" + str(score))
                while checkTable(table):
                    searchConnected(table)
                    score_count(table)
                    drop(table, signal, num)
                    print (table)
                    print("分數:" + str(score))
            else:
                swapy(table, x1, y1, y2, num)
                print("分數:" + str(score))
                while checkTable(table):
                    searchConnected(table)
                    score_count(table)
                    drop(table, signal, num)
                    print (table)
                    print("分數:" + str(score))

if __name__ == '__main__':
    main()



