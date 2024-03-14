def count_substring(string, sub_string) -> int:
    window_size: int = len(sub_string)
    str_len: int = len(string)
    end_index: int = str_len - window_size + 1
    count: int = 0   

    for window_start_pos in range(end_index):
        #print("sub_str {}, window start pos {}, windows size {}, end index {}".format(sub_str, window_start_pos, window_size, end_index))
        sub_str = string[window_start_pos:(window_size + window_start_pos)]
        if (sub_str == sub_string):
            count += 1       

    return count

def main() -> None:
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)

if __name__ == '__main__':
    main()