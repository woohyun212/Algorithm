import sys
count = int(sys.stdin.readline())
divisors = sorted(map(int, sys.stdin.readline().split()))

if count % 2 == 1:
    print(divisors[count//2] ** 2)
else:
    print(divisors[0]* divisors[-1])
    
