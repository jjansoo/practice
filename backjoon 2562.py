listnum = []
for i in range(9):
    listnum.append(int(input()))

print(max(listnum))
print(listnum.index(max(listnum)))