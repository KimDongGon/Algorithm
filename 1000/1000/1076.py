color = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
mul = [10 ** i for i in range(0, 10)]
arr = list(input() for _ in range(3))
print(int(str(color.index(arr[0])) + str(color.index(arr[1]))) * mul[color.index(arr[2])])