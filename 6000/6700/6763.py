a = int(input())
b = int(input())

if a - b >= 0:
    print('Congratulations, you are within the speed limit!')
else:
    num = b - a
    if 1 <= num <= 20:
        f = 100
    elif 21 <= num <= 30:
        f = 270
    else:
        f = 500
    print(f'You are speeding and your fine is ${f}.')