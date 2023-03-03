import sys

# 일반적인 에라토스테네스의 체 알고리즘
array = [True for i in range(1000001)] 
# 체를 만들어 놓고
for i in range(2, 1001): # 구하려는 범위의 루트(n) 까지
    if array[i] == True:
        j = 2  # 제일 작은 소수 2부터
        while i * j <= 1000000:
            array[i * j] = False # 소수의 배수를 False로 변경
            j += 1

while True:
    n = int(sys.stdin.readline())
    if n == 0 : break
    for i in range(2, n+1):  # 제일 작은 소수부터 n 까지 빼보기 시작
        if array[i] and array[n - i]:  
            # 일단 소수가 아니면 다음으로 넘어가면서 확인
            print(f'{n} = {i} + {n - i}')  
            break
            
"""
python3 로는 안되고 pypy3 로는 정답처리 되더라
소수 관련 문제고 시간제한이 0.5초길래
에라토스테네스의 체를 떠올리긴 했는데, 
생각한대로 했는데도 정답처리 되지 못했다.
내가 했던 코드에서 줄일 수 있는 부분을 줄이고 
코드로 해둔 연산을 미리 계산하여 상수로 집어넣었더니
그제서야 정답처리 됐다. 생각해낸 풀이방식은 맞았으나,
제대로 효율성있게 작업하지 못한 것 같다. 채점하기 전에 
어떤 부분을 더 최적화 할 수 있을지 생각해봐야겠다.
"""