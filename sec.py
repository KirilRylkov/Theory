
import math
import numpy
import matplotlib.pyplot

from fir import getInterval
from fir import getX
from fir import getY
from fir import getVariationSeries


def equallyIntervalMethod(Y):
    # выбираем количество интервалов
    if len(Y) <= 100:
        M = int(round(numpy.sqrt(N)))
    else:
        M = int(round(4 * math.log(N, 10)))
    # длинна интервала
    # вычисляется по формуле (Xn-X1)/M
    h = round((Y[-1] - Y[0]) / M, 4)
    # левая и правая граница интервала
    # вычислеяется по формуле X1+(i+1)
    # вычисляется по формуле Ai+1
    A, B = [], []

    A.append(round(Y[0], 4))
    # заполняем списки о по формулам
    for i in range(1, M):
        A.append(round((Y[0] + i * h), 4))
        B.append(A[i])
    B.append(round((Y[0] + M * h), 4))

    # вычисляем среднюю плотномть вероятности
    f = []
    # частота
    frequency = []
    amount = 0
    for i in range(M):
        for j in range(len(Y)):
            # сколько чисел входят в i-тый интервал
            if A[i] <= Y[j] < B[i]:
                amount += 1
        # заносим в список
        frequency.append(round(amount / (N), 4))
        # вычисляем среднюю плотность вероятности для каждого интервала по формуле Fi = Mi /(n*h)
        f.append(round(amount / (N * h), 4))
        amount = 0
    # выводим длинну интервала и границы интервалов среднюю плотность вероятности
    print('h= ', h)
    print('A= ', A)
    print('B= ', B)
    print('F= ', f)
    return A, B, f, M, h, frequency


def plotHist(A, B, F):
    F = [0] + F + [0]
    B = [A[0]] + B + [B[-1]]
    print('F2= ', F)
    print('B2= ', B)
    matplotlib.pyplot.step(B, F)
    matplotlib.pyplot.show()


def plotPoligon(A, B, M, freq):
    ## по X значения середины интервалов по y частаты
    X = []
    for i in range(M):
        # находим середны нтервалов
        X.append((A[i] + B[i]) / 2)
    matplotlib.pyplot.plot(X, freq, label="Полигон")


def plotEmpir(B, freq):
    val = []
    # суммируем значения vali = sum(freg0 ... fregi+1)
    for i in range(len(freq)):
        val.append(sum(freq[:i + 1]))
    x = [-1]
    y = [0, 0]
    for k, v in enumerate(B):
        x.append(v)
        x.append(v)
        y.append(val[k])
        y.append(val[k])
    y.pop()
    x.append(125)
    y.append(1)
    matplotlib.pyplot.plot(x, y, label="Сгруппированная эмпирическая функция")
    matplotlib.pyplot.legend()
    matplotlib.pyplot.show()


def equiprobableMethod(Y):
    # выбираем количество интервалов
    if N <= 100:
        M = int(round(numpy.sqrt(N)))
    else:
        M = int(round(4 * math.log(N, 10)))
    # количество попаданий в каждый интервал
    v = math.ceil(N / M)
    # левая и правая граница интервала
    A, B = [], []
    # Формула A1 = y1
    # Формула B1 = (Yv +Yv+1)/2
    A.append(round(Y[0], 4))
    B.append(round((Y[v] + Y[v - 1]) / 2, 4))
    for i in range(1, M - 1):
        A.append(B[i - 1])
        B.append(round((Y[(v * (i + 1))] + Y[(v * (i + 1) + 1)]) / 2, 4))
    A.append(B[-1])
    B.append(round((Y[-1]), 4))
    # Формула hi = Bi-Ai
    # Формулв fi = v/(n*hi)
    f = []
    for i in range(len(A)):
        f.append(round(v / (N * (B[i] - A[i])), 4))
    freq = [v / N] * M
    print('h= ', f)
    print('A= ', A)
    print('B= ', B)
    print('F= ', freq)
    return A, B, f, M, freq


if __name__ == '__main__':
    N = 10000
    # полчаем интервал
    a, b = getInterval(2, 3 ** (1 / 2))
    # получаем X
    X = getX(a, b, N)
    # получаем Y=x^3
    Y = getY(X)
    # получаем вариационный ряд
    Y = getVariationSeries(Y)

    # равноинтервальный метод
    A, B, F, M, h, freq = equallyIntervalMethod(Y)
    # гистограма
    plotHist(A, B, F)
    # полигон
    plotPoligon(A, B, M, freq)
    # функция
    plotEmpir(B, freq)

    # равновероятностный метод
    A, B, F, M, freq = equiprobableMethod(Y)
    # гистограма
    plotHist(A, B, F)
    # полигон
    plotPoligon(A, B, M, freq)
    # функция
    plotEmpir(B, freq)
