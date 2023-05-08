n = int(input())
s_sum = 0
for i in range(1, 10):
    if n >= 10 ** i:
        s_sum += i * 9 * (10 ** (i - 1))
    else:
        s_sum += i * (n - (10 ** (i - 1)) + 1) 
        break
print(s_sum)
"""
인터넷에서 찾은 더 직관적인 코드

n = int(input())
n_len = len(str(n))
count = 0
for i in range(n_len - 1):
    count += 9 * 10 ** i * (i + 1)
print(count + (n - 10 ** (n_len - 1) + 1) * n_len)


내가 짠건 for 문 하나로 돌아가게 했는데
생각해보니까 else 하나로 break 걸거면
따로 빼도됐었고, 시간이 오래걸린건 >=인지 > 인지 판단이 잘 안섰다.
규칙성은 금방 찾았는데 왜 이렇게 오래걸린거지..
"""