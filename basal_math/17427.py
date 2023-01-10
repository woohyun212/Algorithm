import sys
input = sys.stdin.readline
n = int(input())
print(sum([(n//i) * i  for i in range(1, n+1)]))
        
    