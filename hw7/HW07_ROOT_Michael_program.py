#################################
#   Michael Root
#   Principles of Data Mining
#   CSCI 420
#   Homework 7
#   Dr. Kinsman
#################################

import csv, math

# Cluster class, holds the size of the clusters, the center AKA average record, and name
class cluster:
    size = 1
    center = 0
    name = ""

# Given 2 clusters and the array they are in, print out the smaller one, and make a new
# cluster that is the average of those 2. Re-make the array the clusters are in so the
# 2 that were merged are removed but the newly merged on is added
def mergeClusters(c1, c2, clusterArray):
    if c1.size < c2.size:
        print(c1.size)
    else:
        print(c2.size)

    temp = cluster()
    temp.name = c1.name+"+"+c2.name
    temp.size = c1.size+c2.size
    temp.center = ((c1.center[0]+c2.center[0])/2, (c1.center[1]+c2.center[1])/2, (c1.center[2]+c2.center[2])/2, (c1.center[3]+c2.center[3])/2, (c1.center[4]+c2.center[4])/2, (c1.center[5]+c2.center[5])/2, (c1.center[6]+c2.center[6])/2, (c1.center[7]+c2.center[7])/2, (c1.center[8]+c2.center[8])/2, (c1.center[9]+c2.center[9])/2, (c1.center[10]+c2.center[10])/2, (c1.center[11]+c2.center[11])/2)

    tempClusterArray = clusterArray
    tempClusterArray.remove(c1)
    tempClusterArray.remove(c2)
    tempClusterArray.append(temp)

    return tempClusterArray

# Return the euclidean distance between the centers of 2 clusters
def eucDist(r1, r2):
    if r1 == r2:
        return 10000
    else:
        return math.sqrt(math.pow((r1[0] - r2[0]), 2) + math.pow((r1[1] - r2[1]), 2) + math.pow((r1[2] - r2[2]), 2) + math.pow((r1[3] - r2[3]), 2) + math.pow((r1[4] - r2[4]), 2) + math.pow((r1[5] - r2[5]), 2) + math.pow((r1[6] - r2[6]), 2) + math.pow((r1[7] - r2[7]), 2) + math.pow((r1[8] - r2[8]), 2) + math.pow((r1[9] - r2[9]), 2) + math.pow((r1[10] - r2[10]), 2) + math.pow((r1[11] - r2[11]), 2))

# Given an array of clusters, find the 2 that have the smallest euclidean distance,
# make a cluster that is both of them merged, remove them from the array, and add
# the newly made combined cluster. Then return the new cluster array that is 1 size
# smaller than before
def mergeSmallestClusters(clusterArray):
    smallest = 100000
    secondSmallest = 100001
    minEucDist = 10000000
    for c in clusterArray:
        for d in clusterArray:
            if c != d:
                if eucDist(c.center, d.center) < minEucDist:
                    smallest = c
                    secondSmallest = d
                    minEucDist = eucDist(c.center, d.center)
    # print(smallest.name)
    # print(secondSmallest.name)
    newClusters = mergeClusters(smallest, secondSmallest, clusterArray)
    return newClusters


# initiate:
#       - the cluster list,
#       - the shopper records list for input
#       - the counter for iterating
clusters = [0] * 100
shoppers = [0] * 100
counter = 0

# Open the CSV file and read in the speeds and reckless bit into 2 different
# lists.

# Tuple saved as (ID,           0
#                 milk,         1
#                 petfood,      2
#                 veggies,      3
#                 cereal,       4
#                 nuts,         5
#                 rice,         6
#                 meat,         7
#                 eggs,         8
#                 yogurt,       9
#                 chips,        10
#                 beer,         11
#                 fruit         12
with open('HW_07_SHOPPING_CART_v137.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if row[0] == 'ID':
            a = 1
        else:
            # Don't read in the unique id, we don't need that for clustering
            shoppers[counter] = (int(row[1]), int(row[2]), int(row[3]), int(row[4]), int(row[5]), int(row[6]), int(row[7]), int(row[8]), int(row[9]), int(row[10]), int(row[11]), int(row[12]))
            counter += 1

# Move all the records from the shoopers input int a cluster struct for each record.
# Keep a record of the name AKA what clusters have been adde together.
# Each cluster gets a size of 1, as each cluster starts off as a single record.
# The center of the cluster is just the record values, as none have been merged.
# Add the clusters to the cluster list
counter = 0
for shopper in shoppers:
    name = str(counter)
    temp = cluster()
    temp.name = name
    temp.radius = 0
    temp.center = (shopper[0], shopper[1], shopper[2], shopper[3], shopper[4], shopper[5], shopper[6], shopper[7], shopper[8], shopper[9], shopper[10], shopper[11])
    clusters[counter] = temp
    counter += 1


# While there is more than 1 cluster in total, merge the smallest 2 and print out the smallest
# of those 2.
while (len(clusters) != 3):
    clusters = mergeSmallestClusters(clusters)
    # print(clusters[0].size)
for c in clusters:
    print(c.name)
    print(c.size)
    print(c.center)

