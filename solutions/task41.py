import numpy

Z = numpy.arange(10)

sum = numpy.add.reduce(Z)
sum2 = numpy.sum(Z)

print(sum, sum2)