#Case 1
num = int(input())
listnum = list(map(int,input().split()))
print(min(listnum),max(listnum))

print('*'*45)
#Case 2
num = int(input())
listnum = list(map(int,input().split()))
listnum.sort()
print(listnum[0],listnum[4])