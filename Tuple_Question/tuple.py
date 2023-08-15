
if __name__ == '__main__':
    n = int(input())
    t = tuple(map ( int , input().split()[:2]))
    print(hash(t))
