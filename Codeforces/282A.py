answer, n = 0, int(input())

for x in range(0,n):
    s = input()
    if '+' in s:
        answer+=1
    else:
        answer-=1

print(answer)
