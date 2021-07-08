import random

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

#Open text file
f = open('sample.txt', 'w')

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
card = []
for num in fr.read().split():
    card.append(int(num))

print(card)

fr.close()
