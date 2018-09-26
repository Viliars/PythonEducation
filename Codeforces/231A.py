
# PYTHON
answer, n = 0, int(input())
for x in range(0,n):
    if( sum( [int(y) for y in input().split()] ) >=2):
        answer += 1
print(answer)

# C++
#int n, a, b, c, answer=0;
#cin>>n;
#for(int i=0; i<n; ++i) {
#    cin>>a>>b>>c;
#    if(a+b+c >= 2) ++answer;
#    }
#cout<<answer;
