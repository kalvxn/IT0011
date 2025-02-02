for i in range(1, 6):
    print(' ' * (5 - i) + ''.join(str(x) for x in range(1, i + 1)))

i = 1
while i <= 7:
    print(str(i) * i)
    i += 2