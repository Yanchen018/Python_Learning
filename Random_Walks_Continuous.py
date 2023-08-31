import numpy
import matplotlib.pyplot as plt

t_max = 10
k = 1000
T = numpy.arange(0, t_max, 1.0 / k)
n = 100

random_numbers = numpy.random.randint(0, 2, size=(t_max * k, n))
value = numpy.cumsum(numpy.where(random_numbers == 0, -1, +1), axis=0)
values = value * (1.0 / numpy.sqrt(k))

plt.xlabel('$t$')
plt.ylabel('$B_t$')
plt.plot(T, values)
plt.show()

value_tmax = value[-1, : ] #(row is time , column is stock)
plt.hist(value_tmax, bins = 10)
plt.title('Distribution of $B_{t_{max}}$')
plt.show()
