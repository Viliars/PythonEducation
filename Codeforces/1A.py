from math import ceil

n, m, a = ( int(x) for x in input().split() )

answer = 0
x, y = int(ceil(n/a)), int(ceil(m/a))
#print(x,y)
print(x*y)
