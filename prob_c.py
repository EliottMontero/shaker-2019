
def dist(xa, ya, xb, yb):
    return ((xb-xa)*(xb-xa) + (yb-ya)*(yb-ya))**0.5

def main():
    inp = input()
    words = inp.split()
    xb = float(words[0])
    yb = float(words[1])
    inp = input()
    words = inp.split()
    N = int(words[0])
    T = int(words[1])
    names = [None] * N
    suspects = [None] * N
    pos = [[None]*T for _ in range(N)]
    x = [[None]*T for _ in range(N)]
    y = [[None]*T for _ in range(N)]
    for i in range(0, N):
        names[i] = input()
        for j in range(0, T):
            pos[i][j] = input().split()
            x[i][j] = float(pos[i][j][0])
            y[i][j] = float(pos[i][j][1])

    for i in range(0, N):

        for j in range(0, T-1):
            if dist(x[i][j],y[i][j], xb, yb) + dist(xb, yb, x[i][j+1],y[i][j+1])  < 100:
                suspects[i] = True

    result = ''
    tmp = False
    for i in range(0, N):
        if tmp == False:
            if suspects[i] == True:
                result = result + names[i]
                tmp = True
        else:
            if suspects[i] == True:
                result = result + ' ' + names[i]
    print(result)

main()
