if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    allPermutations = []

    for i in range(0,x+1):
        for j in range(0,y+1):
            for k in range(0,z+1):
                ijkList = [i,j,k]
                allPermutations.append(ijkList)

    reducedList = [xlist for xlist in allPermutations if sum(xlist) != n]

    print(reducedList)
    