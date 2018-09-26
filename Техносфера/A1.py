

def fact(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n*fact(n-1)


if __name__ == '__main__':
    a = int(input())
    print(fact(a))
