#################################
#   Michael Root
#   Principles of Data Mining
#   CSCI 420
#   Homework 2
#   Dr. Kinsman
#################################

import matplotlib.pyplot as plt
import matplotlib.pyplot as varplt
import numpy as np
import csv

plt.figure(1)
plt.ylim([0, 40])
plt.ylabel("Mixed Variance")
plt.xlabel("Threshold")
plt.title("Variance per Threshold")
plt.minorticks_on()

#####
# Part 1
#####

speeds = [0.0] * 128
counter = 0

with open('UNCLASSIFIED_Speed_Observations_for_128_vehicles.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        speeds[counter] = float("{0:.2f}".format(np.double(row[0])))
        counter += 1

bins = []
for bin in range(38, 81, 2):
    bins.append(bin)


best_mixed_variance = 10000000000
best_threshold = -9999

wt_under = 0.00
wt_over = 0.00

var_under = 0
var_over = 0

speeds.sort()

for threshold in bins:

    for fraction in bins:
        if fraction <= threshold:
            wt_under += 1
        else:
            wt_over += 1

    wt_under = wt_under / len(bins)
    wt_over = wt_over / len(bins)

    index = 0
    minFound = False
    for speed in speeds:
        if speed > threshold and minFound == False:
            index = speeds.index(speed)
            minFound = True

    var_under = np.var(speeds[0:index])
    var_over = np.var(speeds[index:])

    mixed_variance = (wt_under * var_under) + (wt_over * var_over)

    varplt.plot(threshold, mixed_variance, marker='.', color='r')

    if mixed_variance < best_mixed_variance:
        best_mixed_variance = mixed_variance
        best_threshold = threshold

print("Best Mixed variance: ", best_mixed_variance)
print("Best Threshold: ", best_threshold, '\n')


#####
# Part 3
#####

unknown_data = [7,8,23,9,8,16,10,22,36,26,10,7,7,12,19,18,6,9,16,12,7,14,18,10,38,28,12,8,9,11,32,19,32,19,18,15,16,20,8,16]
print("Unknown Data Median = ", np.median(unknown_data))
print("Unknown Data Average = ", float("{0:.1f}".format(np.average(unknown_data))),'\n')

unknown_data2 = [7,8,23,9,8,16,10,22,36,26,10,7,7,12,19,18,6,9,16,12,7,14,18,10,38,28,12,8,9,11,32,19,32,19,18,15,16,20,8]
print("Unknown Data 2 Median = ", np.median(unknown_data2))
print("Unknown Data 2 Average = ", float("{0:.1f}".format(np.average(unknown_data2))))



best_mixed_variance = 10000000000
best_threshold = -9999

wt_under = 0.00
wt_over = 0.00

var_under = 0
var_over = 0

unknown_data2.sort()

for threshold in unknown_data2:

    for fraction in unknown_data2:
        if fraction <= threshold:
            wt_under += 1
        else:
            wt_over += 1

    wt_under = wt_under / len(bins)
    wt_over = wt_over / len(bins)

    index = 0
    minFound = False
    for data in unknown_data2:
        if data > threshold and minFound == False:
            index = unknown_data2.index(data)
            minFound = True

    var_under = np.var(unknown_data2[0:index])
    var_over = np.var(unknown_data2[index:])

    mixed_variance = (wt_under * var_under) + (wt_over * var_over)

    if mixed_variance < best_mixed_variance:
        best_mixed_variance = mixed_variance
        best_threshold = threshold

print("\nBest Mixed variance: ", best_mixed_variance)
print("Best Threshold: ", best_threshold, '\n')

plt.figure(2)
plt.hist(speeds, bins, linestyle=('solid'), linewidth=2)
plt.xlabel('Speeds')
plt.ylabel('# of Cars')
plt.title("Histogram of Car Speeds")
plt.minorticks_on()
plt.show()

