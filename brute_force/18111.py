import sys; input = sys.stdin.readline
from collections import Counter

N, M, inv = map(int, input().split())
# 높이 데이터를 counter 로 받기위해서 1차원 데이터로 입력
heights = sum([list(map(int, input().split())) for _ in range(N)],[])
# 좌표는 필요없으니까 높이 데이터를 counter로 변환
counter = Counter(heights).items()
# 답이 되는 경우는 3가지 다
# 1. 이미 쌓여있는 블로 중 가장 높은 블록
#     - 이미 쌓여있는데 굳이 더 쌓을 필요는 없으니까
# 2. 존재하는 블럭으로 세울 수 있는 가장 높은 높이
#     -  특정 부분만 파여 있다거나 한 경우에 다른 곳들을 파내야하니까
# 3. 그럼 답이 가능한 위의 두 높이 중 
#     작은 높이에서 1씩 줄여나가며 가장 높고, 가장 짧은 시간이 답이 됨
highest = min((inv + sum(heights)) // (N * M), max(heights)) 
ans_time = ans_height = 1e9
for height in range(highest, -1, -1):
    time = 0
    for h, ct in counter:
        if height < h: 
            time += (h - height) * ct * 2 
        else: 
            time += (height - h) * ct
    print(height, time)
    if time < ans_time:
        ans_time = time
        ans_height = height
    else:
        continue
        # break
print(ans_time, ans_height)

"""
생각할 시간이 많았더라면 어떘을까 싶은 문제
충분히 생각해 낼 수 있을 거라는 생각이 들었다.
사실 해답을 보고 나서, 나도 굳이 좌표가 중요할까?
높이에 따른 작업 시간만 계산하면되는게 아닐까? 
라는 생각을 하긴했는데 위와 같은 직관적인 알고리즘을
너무 어렵게 생각해서 구현해내지 못하고 문제에서 제시한 작업만
구현해낸게 아쉽다.
"""