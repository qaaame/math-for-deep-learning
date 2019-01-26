a = [0] * 8
a[0] =1
a[1] =1
for i in range(2,8):
    a[i] = a[i -1] + a[i -2]

print(a)

