import math
import numpy
import random
from collections import Counter
import matplotlib.pyplot


# Y = x^3
# математическое ожидание x = 2
# среднеквадратическое отклонение x = 3^(1/2)


# Возвращает интервл случайной велечины
def getInterval(expectation, standardDeviation):
    # Matrix = numpy.array([[1, 1], [-1, 1]])
    # vector = numpy.array([2 * expectation, 2 * math.sqrt(3) * standardDeviation])
    # return numpy.linalg.solve(Matrix, vector)
    a = (2 * expectation - 2 * math.sqrt(3) * standardDeviation) / 2
    b = 2 * math.sqrt(3) * standardDeviation + a
    return [round(a), round(b)]


def getX(a, b, N):
    return [random.random() * (b - a) + a for i in range(N)]


def getY(X):
    return [i ** 3 for i in X]

def getVariationSeries(Y):
    return sorted(Y)

def func(x):
    res = x ** (1 / 3)
    return res


if __name__ == '__main__':
    # количество чисел
    N = 50
    # получаем интервал
    a, b = getInterval(2, 3 ** (1 / 2))
    # получаем список случайных величи равномерно распределённых на интервале a, b
    X = getX(a, b, N)
    # получаем Y=x^3
    Y = getY(X)
    # получаем вариационный ряд
    Y = getVariationSeries(Y)
    # выводим Y
    print(Y)
    # присваиваем в Counter (словарь в котором записываются уникальные элементы и их количество)
    first = Counter(Y)
    # вероятность появления величины
    probability = 0
    # словарь для хранения случайных величин ключ велиина значение вероятность
    second = {}
    for key in first:
        # количество случайной величины  одним значением  делем на общее количество случайных величин
        probability = round(probability + first[key] / len(Y), 4)
        second[key] = probability

    print(second)
    # эмпирическая функция
    x = [-10]
    y = [0, 0]
    # заносим в списки
    for key in second:
        x.append(key)
        x.append(key)
        y.append(second[key])
        y.append(second[key])
    y.pop()
    x.append(135)
    y.append(1)
    # строим график эмпирической функции
    e, = matplotlib.pyplot.plot(x, y)
    #matplotlib.pyplot.plot([-10, -1, 125, 135], [0, 0, 1, 1], 'red')

    # теоритическая функция
    x = [-10]
    y = [0]
    i = 0
    while i != 125:
        x.append(i)
        y.append((func(i) / 5))
        i += 1
    x.append(135)
    y.append(1)
    # строим график теоритической функции
    t, = matplotlib.pyplot.plot(x, y, 'red')
    matplotlib.pyplot.legend([e, t], ['эмпирическая функция','теоритическая функция'])
    matplotlib.pyplot.show()
