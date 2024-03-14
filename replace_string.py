def mutate_string(string, position, character):
    result = ""

    if position <= len(string):
        result = string[:position] + character + string[position+1:]

    return result

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)