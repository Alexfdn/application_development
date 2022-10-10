a = int(input())
for i in range (2, a+1):
    if a % i == 0:
        break
print(i)
b = int(input())
for i in range (1, b + 1):
    if 5 <= i <= 9:
        continue
    if 17 <= i <= 37:
        continue
    if 78 <= i <= 87:
        continue
    print(i)