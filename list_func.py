if __name__ == '__main__':
    N = int(input())
    arraylist = []

    for _ in range(N):
        instr, *line = input().split()
        params = list(map(int, line))
        if (instr == "insert"):
            arraylist.insert(params[0], params[1])
        elif (instr == "print"):
            print (arraylist)
        elif (instr == "remove"):
            arraylist.remove(params[0])
        elif (instr == "append"):
            arraylist.append(params[0])
        elif (instr == "sort"):
            arraylist.sort()
        elif (instr == "pop"):
            arraylist.pop()
        elif (instr == "reverse"):
            arraylist.reverse()
        
        #print("instruction: {}, params {}".format(instr, params))
        #print (arraylist)

