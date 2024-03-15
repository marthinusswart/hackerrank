def contains_alnum (input) -> bool:
    return any(char.isalnum() for char in input)

def contains_alpha (input) -> bool:
    return any(char.isalpha() for char in input)

def contains_num (input) -> bool:
    return any(char.isdigit() for char in input)

def contains_lower (input) -> bool:
    return any(char.islower() for char in input)

def contains_upper (input) -> bool:
    return any(char.isupper() for char in input)
def main() -> None:
    s = input()
    print(contains_alnum(s))
    print(contains_alpha(s))
    print(contains_num(s))
    print(contains_lower(s))
    print(contains_upper(s))

if __name__ == '__main__':
    main()