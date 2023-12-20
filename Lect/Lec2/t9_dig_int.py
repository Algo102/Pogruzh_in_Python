import sys

STEP = 2 ** 16
num = 1
for _ in range(30):
    print(sys.getsizeof(num), num)
    num *= STEP

# getsizeof - размер объекта в байтах в озу
# _ - когда НЕ нужна переменная, но цикл без нее ломается

num = 7_901_123_456 # только для визуализации
print(num)