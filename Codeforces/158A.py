n, k = [int(x) for x in input().split()]

people = [int(x) for x in input().split()]

count = 0

for x in people:
    if x>0 and x>=people[k-1]:
        count+=1

#print(n,k,people)

print(count)
