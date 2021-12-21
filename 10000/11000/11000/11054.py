n = int(input())
nums = [int(x) for x in input().split()]

m = max(nums)

indexes = [i for i, v in enumerate(nums) if v == m]

print(indexes)
