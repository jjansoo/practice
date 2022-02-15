num = int(input())
for i in range(1,num+1):
    a,b = map(int,input().split())
    C= a+b
    print(f'Case #{str(i)}: {a} + {b} = {C}')