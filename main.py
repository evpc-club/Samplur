import numpy as np
import matplotlib.pyplot as plt
import random
plt.rcdefaults()


def inArr(theData, newData):
    for j in range(len(theData)):
        if newData == theData[j]:
            return True
    return False


print("Welcome! Please enter the parameters below when prompted. This program will take a random sample of data from the data set in data.txt and find the mean. This will be repeated to form a bar graph.")
file = []
f = open("data.txt", "r")
for x in f:
    file.append(int(x))
sampleSize = int(input("Please enter the sample size: "))
while sampleSize > len(file):
    sampleSize = int(input("\nPlease try again. Your sample size is larger than the amount of data: "))
numberTimesToRepeat = int(input("\nPlease enter the number of times you want this to repeat: "))
means = []

for i in range(numberTimesToRepeat-1):
    currentTotal = 0
    currentIndexes = []
    currentData = []
    for k in range(sampleSize):
        newInt = random.randint(0, len(file)-1)
        while inArr(currentIndexes, newInt):
            newInt = random.randint(0, len(file)-1)
        currentIndexes.append(newInt)
        currentData.append(file[newInt])
        currentTotal += file[newInt]
    means.append(currentTotal/sampleSize)

graph = [[], []]
means.sort()
for i in range(len(means)):
    means[i] = round(means[i]*10)/10
currentValue = means[0]
graph[0].append(str(currentValue))
graph[1].append(1)
for i in range(len(means)):
    if means[i] == currentValue:
        graph[1][len(graph[1])-1] += 1
    else:
        currentValue = means[i]
        graph[0].append(str(currentValue))
        graph[1].append(1)

xObjects = graph[0]
y_pos = np.arange(len(xObjects))
occurrences = graph[1]

plt.bar(y_pos, occurrences, align='center', alpha=0.5)
plt.xticks(y_pos, xObjects)
plt.ylabel('Occurrences')
plt.title('Statistics')

plt.show()
