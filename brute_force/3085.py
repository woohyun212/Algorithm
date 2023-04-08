import sys
input = sys.stdin.readline
n = int(input())
candy_map = [list(input().rstrip('\n')) for _ in range(int(n))]
steps = [[0, 1],[0, -1],[1, 0],[-1, 0]]
result = 0

for y in range(n):
    for x in range(n):
        for step in steps:
            nx, ny = x+step[0], y+step[1]
            if 0<= nx < n and 0 <= ny < n:
                candy_map[y][x], candy_map[ny][nx] = candy_map[ny][nx], candy_map[y][x]
                max_cnt = 0
                for _y in range(n):
                    cnt = 1 
                    for _x in range(n-1):
                        if candy_map[_y][_x] == candy_map[_y][_x+1]:
                            cnt += 1
                            max_cnt = max(max_cnt, cnt)
                        else:              
                            cnt = 1
                for _x in range(n):
                    cnt = 1
                    for _y in range(n-1):
                        if candy_map[_y][_x] == candy_map[_y+1][_x]:
                            cnt += 1
                            max_cnt = max(max_cnt, cnt)
                        else:              
                            cnt = 1
                result = max(max_cnt, result)
                candy_map[y][x], candy_map[ny][nx] = candy_map[ny][nx], candy_map[y][x]
print(result)

"""
완전탐색 문제인데 어떻게든 시간으르 줄여보고 싶어서 바꿨을 때만, 
바꾼 줄 인근만 변경하도록 코드를 짜보려고 했는데, 이미 PPPP 처럼
완성되어 있는 경우 검사하지 않기 때문에 문제를 틀릴 수 밖에 없었다.
차라리 조금만 다시 생각해서 아무것도 변경되지 않았을 때 최초 검사를 하고
이후에는 변경했을 때만 검사한다면 시간을 단축시킬 수 있었을까 라는 생각이 드는 문제
+
사탕게임... nx 와 step 을 익혀두지 않았다면 조금 귀찮았을 것 같다,
"""