import sys
E, S, M = map(int, sys.stdin.readline().split())
real_year = 1
class celes:
    def __init__(self, period):
        self.period = period
        self.year = 1
    
    def __add__(self, n):
        self.year += n
        if self.year > self.period: # 더하다가 주기를 넘어가면 1로 초기화
            self.year = 1
        return self

        
earth = celes(15)
sun = celes(28)
moon = celes(19)

while E!=earth.year or S!=sun.year or M!=moon.year:
    real_year += 1
    earth += 1
    sun += 1
    moon += 1
print(real_year)

"""
이번 문제는 어떻게 풀어야할지 직감적으로 알았다.
근데 그냥 풀면 재미없을 것 같아서 클래스로 만들어서 풀어봤는데
더 비효율적인가 싶다.
"""