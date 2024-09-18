N = float(input("Введите число N: "))
sum_numbers = 0
for i in range(0, int(N * 10) + 1):
    sum_numbers += 1 + i / 10
print(f"Сумма чисел от 1 до (1 + N/10) равна {sum_numbers}.")
