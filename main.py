import numpy as np
import matplotlib.pyplot as plt
import random
plt.rcdefaults()

def partInRange(first, second, arr):
    returnArr = []
    for z in range(len(arr)):
        if first <= arr[z] < second:
            returnArr.append(arr[z])
    return returnArr

def lenOfStrArr(arr):
    editedArr = arr.copy()
    for z in range(len(arr)):
        editedArr[z] = len(editedArr[z])
    return sum(editedArr)


def lenOfIntArr(arr):
    editedArr = arr.copy()
    for z in range(len(arr)):
        editedArr[z] = len(str(editedArr[z]))
    return sum(editedArr)


def inArr(theData, newData):
    for j in range(len(theData)):
        if newData == theData[j]:
            return True
    return False


file = []
f = open("data.txt", "r")
for x in f:
    file.append(int(x))

sample_size = int(input("Please enter the sample size: ")) #Take the sample

while sample_size > len(file):
    sample_size = int(input("\nPlease try again. Your sample size is larger than the amount of data: "))

repetitions = int(input("\nPlease enter the number of times you want this to repeat: "))
means = []

#Record the means and add to aggregate list
for i in range(repetitions-1):
    currentData = random.sample(file, sample_size)
    means.append(sum(currentData)/sample_size)

graph = [[], []]
means.sort()
for i in range(len(means)):
    means[i] = round(means[i]*10)/10

if lenOfIntArr(means) < 102:
    currentValue = means[0]
    graph[0].append(str(currentValue))
    graph[1].append(1)
    for i in range(len(means)):
        if means[i] == currentValue:
            graph[1][len(graph[1]) - 1] += 1
        else:
            currentValue = means[i]
            graph[0].append(str(currentValue))
            graph[1].append(1)
    plt.figure(1)
    y_pos = np.arange(len(graph[0]))
    plt.bar(y_pos, graph[1], align='center', alpha=0.5)
    plt.xticks(y_pos, graph[0])
    plt.ylabel('Occurrences')
    plt.title('Statistics')
else:
    lastMean = means[len(means) - 1]
    rangeLen = float(int(lastMean)+1-int(means[0]))
    if float(int(lastMean)) == lastMean:
        rangeLen -= 1
    rangeLen = rangeLen/float(14)
    if float(int(rangeLen)) == rangeLen:
        rangeLen = int(rangeLen)
    else:
        rangeLen = int(rangeLen) + 1
    i = int(means[0]) - (int(means[0]) % rangeLen)
    newMeans = []
    newOccurrences = []
    while i <= int(lastMean) - (int(lastMean) % rangeLen):
        newMeans.append(str(i) + "-" + str(i + rangeLen))
        newOccurrences.append(len(partInRange(i, i+rangeLen, means)))
        i += rangeLen
    plt.figure(1)
    y_pos = np.arange(len(newMeans))
    plt.bar(y_pos, newOccurrences, align='center', alpha=0.5)
    plt.xticks(y_pos, newMeans)
    plt.ylabel('Occurrences')
    plt.title('Statistics')
    plt.figure(2)
    y_pos = np.arange(len(newMeans))
    percentOfData = []
    for i in range(len(newOccurrences)):
        percentOfData.append(newOccurrences[i]/sum(newOccurrences)*100)
    plt.bar(y_pos, percentOfData, align='center', alpha=0.5)
    plt.xticks(y_pos, newMeans)
    plt.ylabel('% of Data')
    plt.title('Statistics')


plt.show()
