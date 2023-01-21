import sys
input = sys.stdin.readline
cases = [int(input()) for _ in range(int(input()))]
case_max = max(cases)
nums = [0] * (case_max+2)
for i in range(1, case_max+1):
    for j in range(i, case_max+1, i):
        nums[j] += i;
    nums[i+1] += nums[i]
for case in cases:
    print(nums[case])
    
"""
많은 사람들이 에라토스테네스의 체와 DP를 응용하여,
미리 약수들의 합이 계산된 배열을 만들고,
이를 input에 대응되는 값을 꺼내어 문제를 풀이했다.
그런 방법의 python 풀이는 시간초과가 나서
pypy3로 채점했더니 정답처리 되었다.

배열을 돌면서 약수에 해당되는 인덱스에 i값을 더해주면 
각 인덱스에는 약수들의 합이 구해지고
이전 배열을 그 다음 배열에 더하여 
문제에서말하는 g(x) 를 구하는 방식을 많이들 채택했었다.

채점하고 나서 해당 부분도 줄일 수 있지 않을까 싶어서 
줄여봤지만 시간초과였다.
i 를 다더했으면 이전 인덱스 값을 바로 다음 인덱스에 넘겨주는 것이다.
어차피 앞쪽에 계산은 끝났으니, 반복문 전체를 한번더 순회할 것을 줄일 수 있어서
시간초과를 피할 수 있으리라 생각했다.
"""