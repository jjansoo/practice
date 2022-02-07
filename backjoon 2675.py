S = int(input())
for i in range(S):
    a, b = input().split()
    for j in b:
        print(int(a)*j,end='')
    print()