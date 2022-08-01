if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr=list(set(arr))
    arr.sort()
    runner=arr[-2]
    print(runner)
