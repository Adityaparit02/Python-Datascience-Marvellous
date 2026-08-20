import statistics

data = [6, 7, 8, 9, 10, 11, 12]

variance = statistics.variance(data)          # sample variance
std_dev = statistics.stdev(data)               # sample standard deviation

print("Dataset:", data)
print("Variance:", variance)
print("Standard Deviation:", std_dev)