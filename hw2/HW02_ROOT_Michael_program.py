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

# Set up the graph for the mixed variance plots
plt.figure(1)
plt.ylim([0, 40])
plt.ylabel("Mixed Variance")
plt.xlabel("Threshold")
plt.title("Variance per Threshold")
plt.minorticks_on()

#####
# Part 1
#####

# Make a list of all the speeds we are going to read in
speeds = [0.0] * 128
counter = 0

# Open up the given CSV file and read in the values. Save them
# as floats rounded to 2 decimal points (if this is specified it
# tries to round them in as they are read and messed it up). Also
# keep a counter while going through to make sure we take the right
# amount of values
with open('UNCLASSIFIED_Speed_Observations_for_128_vehicles.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        speeds[counter] = float("{0:.2f}".format(np.double(row[0])))
        counter += 1

# Create a list of values we want to use for the bins of storing
# the values we are given
bins = []
for bin in range(38, 81, 2):
    bins.append(bin)

# Sort the speeds
speeds.sort()

# Set the best variance and threshold
best_mixed_variance = 10000000000
best_threshold = -9999

# Instantiate the variables we will be using to calculate the
# minimum mixed variences
wt_under = 0.00
wt_over = 0.00
var_under = 0
var_over = 0

# Go through all the bin starts
for threshold in bins:

    # Calculate the under and over for the variance calculation
    for fraction in bins:
        if fraction <= threshold:
            wt_under += 1
        else:
            wt_over += 1

    # Get the actual udner and over
    wt_under = wt_under / len(bins)
    wt_over = wt_over / len(bins)

    # Find an index value in the list of speeds to base the
    # under and over variance on. This is the separator of
    # the list of speeds instead of making 2 different arrays
    # to use for the variance.
    index = 0
    minFound = False
    for speed in speeds:
        if speed > threshold and minFound == False:
            index = speeds.index(speed)
            minFound = True

    # Actually calculate the variance based on the separator
    # in the list of speeds
    var_under = np.var(speeds[0:index])
    var_over = np.var(speeds[index:])

    # Calculate the final mixed variance
    mixed_variance = (wt_under * var_under) + (wt_over * var_over)

    # Plot the mixed variances per threshold as calculated
    varplt.plot(threshold, mixed_variance, marker='.', color='r')

    # Save the minimum mixed variance if it is found
    if mixed_variance < best_mixed_variance:
        best_mixed_variance = mixed_variance
        best_threshold = threshold

print("Best Mixed variance: ", best_mixed_variance)
print("Best Threshold: ", best_threshold, '\n')


#####
# Part 3
#####

# First set of given unknown data, find the median and average
unknown_data = [7,8,23,9,8,16,10,22,36,26,10,7,7,12,19,18,6,9,16,12,7,14,18,10,38,28,12,8,9,11,32,19,32,19,18,15,16,20,8,16]
print("Unknown Data Median = ", np.median(unknown_data))
print("Unknown Data Average = ", float("{0:.1f}".format(np.average(unknown_data))),'\n')

# Second set of unknown data, identical to the one above but without
# the last 16 listed
unknown_data2 = [7,8,23,9,8,16,10,22,36,26,10,7,7,12,19,18,6,9,16,12,7,14,18,10,38,28,12,8,9,11,32,19,32,19,18,15,16,20,8]
print("Unknown Data 2 Median = ", np.median(unknown_data2))
print("Unknown Data 2 Average = ", float("{0:.1f}".format(np.average(unknown_data2))))


# Run Otsu's method on the 2nd set of unknown data
best_mixed_variance = 10000000000
best_threshold = -9999

# instantiate the unknown variables
wt_under = 0.00
wt_over = 0.00
var_under = 0
var_over = 0

# Sort the data
unknown_data2.sort()

# go through every threshold of the data (every data point)
for threshold in unknown_data2:

    # Get the amount over and under the threshold
    for fraction in unknown_data2:
        if fraction <= threshold:
            wt_under += 1
        else:
            wt_over += 1

    # Get the actual over and under variables
    wt_under = wt_under / len(bins)
    wt_over = wt_over / len(bins)

    # Find the separator in unknown data
    index = 0
    minFound = False
    for data in unknown_data2:
        if data > threshold and minFound == False:
            index = unknown_data2.index(data)
            minFound = True

    # Calculate the variances
    var_under = np.var(unknown_data2[0:index])
    var_over = np.var(unknown_data2[index:])

    # Calculate the total mixed variance
    mixed_variance = (wt_under * var_under) + (wt_over * var_over)

    # See if it is smaller
    if mixed_variance < best_mixed_variance:
        best_mixed_variance = mixed_variance
        best_threshold = threshold

print("\nBest Mixed variance: ", best_mixed_variance)
print("Best Threshold: ", best_threshold, '\n')

# Plot out the histogram of the speeds in their bins
plt.figure(2)
plt.hist(speeds, bins, linestyle=('solid'), linewidth=2)
plt.xlabel('Speeds')
plt.ylabel('# of Cars')
plt.title("Histogram of Car Speeds")
plt.minorticks_on()
plt.show()

