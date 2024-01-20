import random as rnd

print(rnd.random()) # Вызвали рандом
# rnd.seed(42) # Задали отправную точку
state = rnd.getstate() # Фиксанули положение
print(rnd.random()) # Вызвали рандом
# rnd.setstate(state) # Вернули к сохраненному положению
print(rnd.random()) # Вызвали рандом. Результат повторился


START = -100
STOP = 1_000
STEP = 10
data = [2, 4, 6, 8, 42, 73]

print('---------------------')
print(rnd.randint(START, STOP)) # Случайное целое в диапозоне
print(rnd.uniform(START, STOP)) # Случайное вещественное в диапозоне
print(rnd.choice(data)) # Случайный элемент последовательности
print(rnd.randrange(START, STOP, STEP)) # Число из диапозона с шагом
print(data) # Показали список
rnd.shuffle(data)
print(data)
print(rnd.sample(data, 2))
print(rnd.sample(data, 2, counts=[1, 1, 1, 1, 1, 100]))