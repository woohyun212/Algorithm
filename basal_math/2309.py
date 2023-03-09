import sys
dwarfs = [int(sys.stdin.readline()) for _ in range(9)]
sum_dwarfs = sum(dwarfs)
def solution():
    for i in range(8):
        for j in range(i+1,9):
            if sum_dwarfs - dwarfs[i] - dwarfs[j] == 100:
                del dwarfs[i]
                del dwarfs[j-1]
                return
solution()
for i in sorted(dwarfs):
    print(i)

"""
문제를 보자마자 어떻게 풀어야할지 감이옴.
나쁘지 않은 감이였는데, 너무 쉬웠다.
그냥 브루트포스문제ㅇㅇ.
"""