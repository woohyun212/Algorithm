import sys
input = sys.stdin.readline
cases = [int(input()) for _ in range(int(input()))]
case_max = max(cases)
nums = [0] * (case_max+2)
for i in range(1, case_max+1):
    for j in range(i, case_max+1, i):
        nums[j] += i;
    nums[i+1] += nums[i]
# for i in range(2, case_max+1):
#     nums[i] += nums[i-1]
for case in cases:
    print(nums[case])