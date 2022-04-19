# Write a procedure to find min, max, mean, standard deviation, variance of number list.
# Example
# Input: 10 50 80 70 49 23 11 4
# output: 4 80 37.13 27.25 848.70

from re import A
import statistics
import pandas as pd

sr = pd.Series([10, 25, 3, 25, 24, 6])

mean = sr.mean()
median = sr.median()
mode = sr.mode()
range1 = sr.max() - sr.min();
stdeviation = sr.std(axis=0, skipna=True)

print(mean)
print(median)
print(mode)
print(range1)
print(stdeviation)
print("Variance of sample set is % s"
      % (statistics.variance(sr)))


