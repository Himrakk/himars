numbers = [759, 805, 808, 405, 504, 706, 230, 5300, 6007, 9078]

numbers = sorted(numbers, reverse=True)


for i in range(len(numbers)):
    for h in range(i + 1, len(numbers)):
        for k in range(h + 1, len(numbers)):
            a = numbers[i]
            b = numbers[h]
            c = numbers[k]
            if a + b > c and c + b > a and a + c > b:
                p = (a + b + c) / 2
                s = (p * (p - a) * (p - c) * (p - b)) ** (1 / 2)

print(s)