import sys
input = sys.stdin.readline

ans = 0 
cases = [10]# [int(input()) for _ in range(int(input()))]
case_max = max(cases)

nums = [0] * (case_max+1)
for i in range(1, case_max+1):
    for j in range(1, case_max+1, i):
        print(i, j)
        nums[j] += i
    nums[i] += nums[i-1]
print(nums)