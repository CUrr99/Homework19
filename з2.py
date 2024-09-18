K = int(input('Введите число K:'))
N = int(input('Введите число N:'))
if K <= N:
   for number in range(K, N + 1):
       print(number)
else:
    for number in range(K, N,-1, - 1):
        print(number)
    

