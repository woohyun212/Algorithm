import sys

while True:
    try:
        n = input()
        if n == "":
            break
        n = int(n)
        ones = 0
        i = 0
        while True:
            ones += 10 ** i
            if ones % n == 0:
                break       
            i += 1
        print(i+1)
    except EOFError:
        break