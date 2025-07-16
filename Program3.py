def generate_series_v2(a):
    result = []
    for i in range(1, 2 * a, 2):
        result.append(i)
        if len(result) == (a if a % 2 else a - 1):
            break
    return result

a = int(input("Enter value: "))
print(generate_series_v2(a))
