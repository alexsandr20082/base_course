import time
M = int(input("Введите значение M: "))
N = int(input("Введите значение N: "))

start_time = time.time()

for i in range(M):
    for j in range(N):
        print(f"Внешний цикл: {i}, Внутренний цикл: {j}")
        time.sleep(1)  

end_time = time.time()
total_time = end_time - start_time
print(f"Общее время работы конструкции: {total_time} секунд.")