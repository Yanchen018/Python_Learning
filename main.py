import numpy as np
from numpy.random import randint, normal, uniform
import matplotlib.pyplot as plt
from numpy import diff, log, cumsum


def simulate_randomWalk():
    y = 0

    max_t = 100 # time values
    movements = randint(0, 2, size = max_t)

    values = [y]
    for movement in movements:
        if movement == 1:
            y = y + 1
        else:
            y = y - 1
        values.append(y)

    plt.xlabel('t')
    plt.ylabel('y')

    plt.plot(values)
    plt.show()


def simulate_cumulativeSum():
    y = 0

    max_t = 100  # time values
    random_numbers = randint(0, 2, size=max_t)
    steps = np.where(random_numbers == 0, -1, +1)
    values = np.cumsum(steps)

    plt.xlabel('t')
    plt.ylabel('y')

    plt.plot(np.concatenate(([0], values)))
    plt.show()

def multiple_realisations():

    t_max = 100
    n = 10
    random_numbers = randint(0, 2, size = (t_max, n))
    steps = np.where(random_numbers == 0, -1, +1)

    values = np.cumsum(steps, axis=0)
    values = np.concatenate((np.matrix(np.zeros(n)), values), axis = 0)
    plt.xlabel('t')
    plt.ylabel('price')
    plt.plot(values)
    plt.show()


def multiplicative_randomWalk():

    initial_value = 100
    t_max = 100
    random_numbers = normal(1, 0.005, size = t_max)
    # random_numbers2 = normal(size = t_max) * 0.005
    # multipliers = 1 + random_numbers2
    values = initial_value * np.cumprod(random_numbers)
    # values2 = initial_value * np.cumprod(multipliers)
    # plt.xlabel('time')
    # plt.ylabel('price')
    # plt.plot(np.concatenate(([100],values)))
    # plt.plot(np.concatenate(([100], values2)))
    # plt.show()
    price = values
    log_returns = diff(log(price))
    plt.xlabel('time')
    plt.ylabel('log-return')

    plt.plot(np.concatenate(([0],log_returns)))
    plt.show()


def randomWalk_logReturn():
    # r means log-return of stocks
    t_max = 100
    n_max = 10
    volatility = 1e-2
    initialvalue = 100.
    r = normal(0, volatility, size = (t_max, n_max))
    values = np.exp(cumsum(r, axis=0)) * initialvalue
    plt.xlabel('$t$')
    plt.ylabel('$y_t$')
    plt.plot(np.concatenate((np.matrix([initialvalue] * n_max), values)))
    plt.show()

def main():

    # simulate_randomWalk()
    # simulate_cumulativeSum()
    # multiple_realisations()
    # multiplicative_randomWalk()
    randomWalk_logReturn()



if __name__ == "__main__":
    main()