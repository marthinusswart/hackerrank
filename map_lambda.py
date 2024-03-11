cube = lambda x: x*x*x

def fibonacci(n):
    # return a list of fibonacci numbers
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n]

if __name__ == '__main__':
    N = int(input())
    print(list(map(cube, fibonacci(N))))