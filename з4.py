K = int(input("Введите число K: "))
N = int(input("Введите число N: "))
sum_even_numbers = 0
for number in range(K, N + 1):
    if number % 2 == 0: 
        sum_even_numbers += number
        print(f"Сумма четных чисел от {K} до {N} включительно равна {sum_even_numbers}.")
