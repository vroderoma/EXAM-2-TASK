da = int(input())
c = 0
for i in range(1,da):
    if da / i == i:
        c += 1
if c == 1: 
    print('True')
else:
    print('False')
