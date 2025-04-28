def numbers_sum(num):
    return sum(map(int, num))


numbers = input().split()

print(*sorted(numbers, key = numbers_sum))
