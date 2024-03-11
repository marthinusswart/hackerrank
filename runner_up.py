if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    arr = list(arr)
    highest = max(arr)    
    runnerUpList = [x for x in arr if x < highest]
    runnerUp = max(runnerUpList)

    print(highest)    
    print(runnerUp)

