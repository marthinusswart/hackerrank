if __name__ == '__main__':
    elements = int(input())    
    params = list(input().split())

    the_tuple = tuple(int(x) for x in params)        
    hashVal = hash(the_tuple)

    print(abs(hashVal))