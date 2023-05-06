import sys
input = sys.stdin.readline
sys.setrecursionlimit(50*2500)


def moveField(x, y):
    if (x, y) in visited:  # 방문 했다면 종료
        return
    visited.add((x, y))  # 아니면 방문한 노드에 추가
    for direction in directions:  # 주변 노드 탐색
        nx, ny = x+direction[0], y+direction[1]
        #  주변 노드가 양배추가 있는 노드면서, 방문하지 않았다면
        if (nx, ny) in cabbages and (nx, ny) not in visited:
            moveField(nx, ny)  # 해당 노드로 이동
        else:
            continue
    return  # 다 찾았으면 종료


directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
for case in range(int(input())):
    count = 0
    M, N, K = map(int, input().split())
    # 양배추 x,y 좌표
    cabbages = {tuple(map(int, input().split())) for _ in range(K)}
    visited = set({})  # 방문한 좌표
    for x, y in cabbages:  # 양배추가 있는 좌표를 가져옴
        if (x, y) in visited:  # 방문했다면 넘기기
            continue
        else:  # 방문 안했으면
            moveField(x, y)  # 해당 밭(노드)으로 이동
            count += 1  # 인접 노드 수색을 다했다면 지렁이 개수 1증가
    print(count)


"""
dfs를 잘못생각하고있었던 것 같다.
생각을 해보니까 지도를 만들 필요도 없는 문제였는데, 괜히 먼저 코드짜다가 길을 잘못들어서
다시 구상하느라 시간이 더걸렸다.그런데 막상 코드로 구현하니까 몇줄안되서 스스로 좀 아쉬움이 컸다.
제출하는데 RecursionError 가 발생해서 당황했는데, 재귀함수 최대 깊이를 초과해서 에러가 난 것이다.
BOJ 서버내에서 sys.setrecursionlimit 이 기본적으로 1000 이었다.
sys.setrecursionlimit(50*2500) 으로 해결했다.
다음부터는 최대 깊이를 생각해서 제한을 미리 설정해야겠다.

다른 사람 풀이 보니까 0과 1을 이용하여 문제에서 제시한 graph를 만들어서 풀었다.
하지만 나는 인접한 노드들의 묶음만 계산하면 된다고 생각해서 노드의 방문만 생각했는데,
내가 잘못한건지 의문이 든다.
"""
