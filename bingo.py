import random
#Siyayi
#initiating each bingo column
B = []
I = []
N = []
G = []
O = []

#Function that randomizes array based on specific parameters

def column(x,y):
    z = []
    for i in range(x,y):
        z.append(i)
    random.shuffle(z)
    return z

#each column has randomized array
B = column(1,16)
I = column(16,31)
N = column(31,46)
G = column(46,61)
O = column(61,76)
call = column(1, 76)
#Hannah
#Open text file
f = open('sample.txt', 'w')

#Writing in each of the individual numbers of the bingo card and call list into a txt file
x = 0
while x <= 4:
    if x == 2:
        f.write(str(B[x]))
        f.write(" ")
        f.write(str(I[x]))
        f.write(" ")
        f.write("0 ")
        f.write(str(G[x]))
        f.write(" ")
        f.write(str(O[x]))
        f.write("\n")
    else:
        f.write(str(B[x]))
        f.write(" ")
        f.write(str(I[x]))
        f.write(" ")
        f.write(str(N[x]))
        f.write(" ")
        f.write(str(G[x]))
        f.write(" ")
        f.write(str(O[x]))
        f.write("\n")
    x += 1



#creates a list of all the numbers that will be called in a randomized order.
for i in call:
    f.write(str(i))
    f.write(" ")

f.close()

fr = open("sample.txt", "r")
card = [[], [], [], [], []]
num = []
callList = []

for i in fr.read().split():
    num.append(int(i))

#function that puts bingo card into 2d array
def makeCard(x, y, z):
    for i in range(x, y):
        card[z].append(num[i])


makeCard(0, 5, 0)
makeCard(5, 10, 1)
makeCard(10, 15, 2)
makeCard(15, 20, 3)
makeCard(20, 25, 4)

for i in range(25, 100):
    callList.append(num[i])
#function goes through all numbers in call list, if the the number is match the bingo card and meets one of the winning condition it is stored in an array
#First array that meets one of the winning conditions will return the final num in the array
#Matthews
def playGame(card, callList):
    result = []
    for i in callList:
        for x in range(0, 5):
            for y in range(0, 5):
                if card[x][y] == i:
                    result.append(i)
    ans1 = []
    ans2 = []
    ans3 = []
    ans4 = []
    ans5 = []
    ans6 = []
    ans7 = []
    ans8 = []
    ans9 = []
    ans10 = []
    ans11 = []
    ans12 = []
    ans13 = []
    for w in result:
        y = 4
        z = 0
        for x in range(0, 5):
            if card[0][x] == w:                   #First four conditions are for the columns
                ans1.append(card[0][x])
                if len(ans1) == 5:
                    return ans1[4]
            if card[1][x] == w:
                ans2.append(card[1][x])
                if len(ans2) == 5:
                    return ans2[4]
            if card[2][x] == w:
                ans3.append(card[2][x])
                if len(ans3) == 4:
                    return ans3[3]
            if card[3][x] == w:
                ans4.append(card[3][x])
                if len(ans4) == 5:
                    return ans4[4]
            if card[4][x] == w:
                ans5.append(card[4][x])
                if len(ans5) == 5:
                    return ans5[4]
            if card[x][0] == w:                 #Next four conditions are for the rows
                ans6.append(card[x][0])
                if len(ans6) == 5:
                    return ans6[4]
            if card[x][1] == w:
                ans7.append(card[x][1])
                if len(ans7) == 5:
                    return ans7[4]
            if card[x][2] == w:
                ans8.append(card[x][2])
                if len(ans8) == 4:
                    return ans8[3]
            if card[x][3] == w:
                ans9.append(card[x][3])
                if len(ans9) == 5:
                    return ans9[4]
            if card[x][4] == w:
                ans10.append(card[x][4])
                if len(ans10) == 5:
                    return ans10[4]
            if card[x][x] == w:                #Final 3 are for the diagnoal winning condition and the four corners winning condition.
                ans11.append(card[x][x])
                if len(ans11) == 4:
                    return ans11[3]
            if card[x][y] == w:
                ans12.append(card[x][y])
                if len(ans12) == 4:
                    return ans12[3]
            if x % 4 == 0 and z % 4 == 0 or x % 4 == 0 and y % 4 == 0:
                if card[x][z] == w:
                    ans13.append(card[x][z])
                elif card[x][y] == w:
                    ans13.append(card[x][y])
                    if len(ans13) == 4:
                        return ans13[3]
            y -= 1
            z += 1


playGame(card, callList)

fr.close()
