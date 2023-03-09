import sys
input = sys.stdin.readline
n = int(input())
candy_map = [list(input().rstrip('\n')) for _ in range(int(n))]

for y in range(n):
    for x in range(n-1):
        if candy_map[y][x] != candy_map[y][x+1]:
            candy_map[y][x], candy_map[y][x+1] = candy_map[y][x+1], candy_map[y][x]

"""
졸리니까 일단 자고일어나서 내일다시
"""
            