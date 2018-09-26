


s = input().lower()

for x in s:
    if x in ["a", "o", "y", "e", "u", "i"]:
        s = s.replace(x,'')
answer = ''
for x in s:
    answer += '.' + x  

print(answer)
        

