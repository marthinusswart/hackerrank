def split_and_join(line):
   array = line.split(" ") 
   result = "-".join(array)
   return result

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)