import numpy as np
import matplotlib.pyplot as plt
import random
from enum import Enum
plt.rcdefaults()


class Mode(Enum):
    PERCENT_IN = 1
    DATA_IN = 2


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


print("Welcome!")
print("Please enter the parameters below when prompted.")
print("This program will take a random sample of data from the data set in data.txt and find the mean.")
print("This will be repeated to form a bar graph.")
print("If there are too many bars, the program will create multiple bar graphs so that you can easily read the x-axis.")
file = []
f = open("data.txt", "r")
mode = Mode.DATA_IN
sampleSize = 0
if int(input("\nIs your input:\n1. Percentages\n2. Raw Data\n")) == 1:
    mode = Mode.PERCENT_IN
if mode == Mode.PERCENT_IN:
    fileDict = {}
    maxDecimals = 0
    for x in f:
        inFromFile = x.split(sep=" ")
        inFromFile[1] = inFromFile[1].rstrip()
        if inFromFile[0] in fileDict:
            fileDict[inFromFile[0]] = float(fileDict[inFromFile[0]]) + float(inFromFile[1])
        else:
            fileDict[inFromFile[0]] = float(inFromFile[1])
        try:
            decimalsInNum = len(inFromFile[1].split(sep=".")[1])
        except IndexError:
            decimalsInNum = 0
        if decimalsInNum > maxDecimals:
            maxDecimals = decimalsInNum
    for x in fileDict:
        fileDict[x] = round(float(fileDict[x]) * (10 ** maxDecimals))
        for y in range(int(fileDict[x])):
            file.append(float(x))
    sampleSize = int(input("\nEnter the sample size: "))
    powerOfTenToMultiplyBy = 0
    while sampleSize > len(file) * (10**powerOfTenToMultiplyBy):
        powerOfTenToMultiplyBy += 1
    x = 0
    while x < powerOfTenToMultiplyBy:
        savedFile = file.copy()
        file = []
        for y in range(10):
            file += savedFile
        x += 1
else:
    for x in f:
        file.append(int(x))
    sampleSize = int(input("\nEnter the sample size: "))
    while sampleSize > len(file):
        sampleSize = int(input("\nPlease try again. Your sample size is larger than the amount of data: "))

numberTimesToRepeat = int(input("\nPlease enter the number of times you want this to repeat: "))
means = []

for i in range(numberTimesToRepeat):
    currentData = random.sample(file, sampleSize)
    means.append(sum(currentData)/sampleSize)

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