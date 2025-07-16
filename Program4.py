def count_multiples(arr):
    result = {i: 0 for i in range(1, 10)}
    for num in arr:
        for i in range(1, 10):
            if num % i == 0:
                result[i] += 1
    return result

arr = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]
print(count_multiples(arr))
